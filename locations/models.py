from django.db import models
from django.db.models import Count, Q


class CountryManager(models.Manager):
    def delete_by_id(self, id):
        country = self.get(id=id)
        if self.is_related_to_profiles(country):
            return False
        country.delete()
        return True

    def is_related_to_regular_profile(self, country):
        cities = country.cities.all()
        return City.objects.get_cities_related_to_regular_profiles_or_not_related_to_any(cities).count()

    def is_related_to_profiles(self, country):
        cities = country.cities.all()
        return City.objects.get_cities_related_to_profiles(cities).count()

    def safe_get_by_name(self, name):
        try:
            country = Country.objects.get(name=name)
        except self.model.DoesNotExist:
            country = None
        return country

    def get_all(self):
        return self.all()

    def create_country_from_json(self, country):
        return self.create(name=country['name'])

    def create_country_with_city_from_file(self, name, country_name, utc):
        return self.get_or_create(name=country_name)[0].cities.create(name=name, utc=utc)


class Country(models.Model):
    name = models.CharField(unique=True, max_length=100)

    objects = CountryManager()

    def __str__(self):
        return self.name

    def can_delete(self):
        cities_count = self.cities.count()
        if not cities_count:
            return True
        return False


class CityManager(models.Manager):
    def get_all(self):
        return self.all()

    def delete_by_id(self, id):
        city = self.get(id=id)
        if self.is_related_to_profiles(city):
            return False
        city.delete()
        return True

    def is_related_to_regular_profile(self, city):
        return city.regularuserprofile_set.count()

    def is_related_to_profiles(self, city):
        return city.regularuserprofile_set.count() or city.psychologistuserprofile_set.count()

    def get_cities_related_to_profiles(self, cities):
        return cities.annotate(
                Count('psychologistuserprofile'),
                Count('regularuserprofile')).filter(
                Q(psychologistuserprofile__count__gt=0) | Q(regularuserprofile__count__gt=0))

    def get_cities_related_to_regular_profiles_or_not_related_to_any(self, cities):
        return cities.annotate(
                Count('psychologistuserprofile'),
                Count('regularuserprofile')).filter(
                Q(psychologistuserprofile__count=0) | Q(regularuserprofile__count__gt=0))

    def get_cities_related_to_psy_profiles_or_not_related_to_any(self, cities):
        return cities.annotate(
                Count('psychologistuserprofile'),
                Count('regularuserprofile')).filter(
                Q(psychologistuserprofile__count__gt=0) | Q(regularuserprofile__count=0))


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
    utc = models.CharField(max_length=10)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'country'], name='the city must be unique within the country')
        ]

    objects = CityManager()

    def __str__(self):
        return self.name
