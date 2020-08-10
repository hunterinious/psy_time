from django.db import models


class Country(models.Model):
    name = models.CharField(unique=True, max_length=50)


class City(models.Model):
    name = models.CharField(unique=True, max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
