from django.db import models
from django.db.models import Count, Q


class CountryManager(models.Manager):
    def get_countries(self):
        return self.all()


class Country(models.Model):
    name = models.CharField(unique=True, max_length=50)

    objects = CountryManager()

    def __str__(self):
        return self.name


class CityManager(models.Manager):
    def get_cities(self):
        return self.all()

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

    def is_related_to_regular_user_profile(self):
        return self.regularuserprofile_set.count()

    def is_related_to_profiles(self):
        return self.regularuserprofile_set.count() or self.psychologistuserprofile_set.count()

