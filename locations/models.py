from django.db import models
from django.db.models import Count, Q
from django.core.validators import MinLengthValidator
from datetime import datetime
from pytz import timezone
import json


class BaseManager(models.Manager):
    def get_all(self):
        return self.all()

    def delete_by_id(self, id):
        object = self.get(id=id)
        if self.is_related_to_profiles(object):
            return False
        object.delete()
        return True


class CountryManager(BaseManager):
    def get_first_city_of_the_country(self, country):
        return country.cities.first()

    def get_timezones_of_the_country(self, counrty):
        return counrty.timezones.all()

    def is_related_to_regular_profile(self, country):
        timezones = country.timezones.all()
        return Timezone.objects.get_related_to_regular_profiles_or_not_related_to_any(timezones).count()

    def is_related_to_profiles(self, country):
        timezones = country.timezones.all()
        return Timezone.objects.get_related_to_profiles(timezones).count()

    def safe_get_by_name(self, name):
        try:
            country = self.get(name=name)
        except self.model.DoesNotExist:
            country = None
        return country

    def create_country_from_json(self, country):
        return self.create(name=country['name'])

    def create_countries_and_timezones_from_json(self):
        with open('static/files/countries_extended.json') as f:
            countries = []
            timezones = []
            for obj in json.load(f):
                country, zones = self.create_country_with_timezones(name=obj['name'],
                                                                    timezones=obj['timezones'],
                                                                    )
                countries.append(country)
                timezones.append(zones)

            return countries, timezones

    def create_country_with_timezones(self, name, timezones):
        country = self.create(name=name)
        zones = []
        for z in timezones:
            zone = Timezone(name=z, country=country)
            zone.offset = zone.calculate_offset(z)
            zones.append(zone.save())
        return country, zones


class Country(models.Model):
    name = models.CharField(unique=True, max_length=100)

    objects = CountryManager()

    def __str__(self):
        return self.name

    def can_delete(self):
        return not self.timezones.count()


class CountryDependentModelManager(BaseManager):
    def is_related_to_regular_profile(self, obj):
        return obj.regularuserprofile_set.count()

    def is_related_to_profiles(self, obj):
        return obj.regularuserprofile_set.count() or obj.psychologistuserprofile_set.count()

    def get_related_to_profiles(self, queryset):
        return queryset.annotate(
                Count('psychologistuserprofile'),
                Count('regularuserprofile')).filter(
                Q(psychologistuserprofile__count__gt=0) | Q(regularuserprofile__count__gt=0))

    def get_related_to_regular_profiles_or_not_related_to_any(self, queryset):
        return queryset.annotate(
                Count('psychologistuserprofile'),
                Count('regularuserprofile')).filter(
                Q(psychologistuserprofile__count=0) | Q(regularuserprofile__count__gt=0))

    def get_related_to_psy_profiles_or_not_related_to_any(self, queryset):
        return queryset.annotate(
                Count('psychologistuserprofile'),
                Count('regularuserprofile')).filter(
                Q(psychologistuserprofile__count__gt=0) | Q(regularuserprofile__count=0))


class CityManager(CountryDependentModelManager):
    pass


class City(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'country'], name='the city must be unique within the country')
        ]

    objects = CityManager()

    def __str__(self):
        return self.name

    def can_delete(self):
        return City.objects.is_related_to_profiles(self)


class TimezoneManager(CountryDependentModelManager):
    pass


class Timezone(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, validators=[MinLengthValidator(3)])
    offset = models.CharField(max_length=6, null=False, blank=True, validators=[MinLengthValidator(5)])
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='timezones')

    def calculate_offset(self, name=None):
        if not name:
            name = self.name
        offset = datetime.now(timezone(name)).strftime('%z')
        return f'{offset[:3]}:{offset[3:]}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'country'], name='the timezone must be unique within the country')
        ]

    objects = TimezoneManager()

    def __str__(self):
        return f'{self.name} ({self.offset})'
