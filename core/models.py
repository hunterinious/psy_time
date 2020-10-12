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
    status = models.CharField(max_length=50, choices=Status.choices)
