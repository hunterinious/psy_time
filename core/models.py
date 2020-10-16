from django.db import models
from django.utils.translation import gettext_lazy as _


class Help(models.Model):
    class Status(models.TextChoices):
        PENDING = 'P', _('Pending')
        IN_PROCESS = 'I', _('In the process')
        CLOSED = 'C', _('Closed')

    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    theme = models.CharField(max_length=255)
    message = models.TextField()
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.PENDING)


class WorldCountryManager(models.Manager):
    def get_countries(self):
        return self.model.objects.all()

    def create_country_from_json(self, country):
        self.model.objects.create(name=country['name'], code=country['code'])


class WorldCountry(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

    objects = WorldCountryManager()