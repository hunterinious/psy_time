from django.db import models
from django.db.models import Count, Q


class CountryManager(models.Manager):
    def safe_get_by_name(self, name):
        try:
            country = Country.objects.get(name=name)
        except self.model.DoesNotExist:
            country = None
        return country

    def get_countries(self):
        return self.all()


class Country(models.Model):
    name = models.CharField(unique=True, max_length=50)

    objects = CountryManager()

    def __str__(self):
        return self.name


class CityManager(models.Manager):
    def get_all(self):
        return self.all()

    def delete_by_name(self, name):
        city = self.get(name=name)
        if self.is_related_to_profiles(city):
            return False
        city.delete()
        return True

    def is_related_to_regular_user_profile(self, city):
        return city.regularuserprofile_set.count()

    def is_related_to_profiles(self, city):
        return city.regularuserprofile_set.count() or city.psychologistuserprofile_set.count()

    def get_cities_not_related_to_profiles(self):
        return self.annotate(
                Count('psychologistuserprofile'),
                Count('regularuserprofile')).filter(
                Q(psychologistuserprofile__count__gt=0) | Q(regularuserprofile__count=0))


class City(models.Model):
    name = models.CharField(unique=True, max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')

    objects = CityManager()

    def __str__(self):
        return self.name

