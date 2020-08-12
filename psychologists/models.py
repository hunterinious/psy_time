from django.db import models
from users.models import PsychologistUser
from locations.models import City


class PsychologistStatus(models.Model):
    name = models.CharField(unique=True, max_length=50)


class PsychologistWorkFormat(models.Model):
    name = models.CharField(unique=True, max_length=50)


class PsychologistTheme(models.Model):
    name = models.CharField(unique=True, max_length=50)


class PsychologistApproach(models.Model):
    name = models.CharField(unique=True, max_length=50)


class PsychologistSpecialization(models.Model):
    name = models.CharField(unique=True, max_length=50)


class PsychologistEducation(models.Model):
    name = models.CharField(unique=True, max_length=50)


class PsychologistSecondaryEducation(models.Model):
    name = models.CharField(unique=True, max_length=50)


class PsychologistLanguage(models.Model):
    name = models.CharField(unique=True, max_length=50)


class PsychologistUserProfile(models.Model):
    avatar = models.ImageField(null=False, blank=False, default="avatars/psy_avatar.jpg")
    birth_date = models.DateField(null=False, blank=False)
    about = models.TextField(null=False, blank=False)
    work_experience = models.TextField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    duration = models.IntegerField(null=False, blank=False)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    user = models.OneToOneField(PsychologistUser, on_delete=models.CASCADE)
    statuses = models.ManyToManyField(PsychologistStatus, related_name="profiles")
    formats = models.ManyToManyField(PsychologistWorkFormat, related_name="profiles")
    themes = models.ManyToManyField(PsychologistTheme, related_name="profiles")
    approaches = models.ManyToManyField(PsychologistApproach, related_name="profiles")
    specializations = models.ManyToManyField(PsychologistSpecialization, related_name="profiles")
    educations = models.ManyToManyField(PsychologistEducation, related_name="profiles")
    secondary_educations = models.ManyToManyField(PsychologistSecondaryEducation, related_name="profiles")
    languages = models.ManyToManyField(PsychologistLanguage, related_name="profiles")


class Image(models.Model):
    name = models.CharField(unique=True, max_length=255)
    image = models.ImageField(null=False, blank=False)
    profile = models.ForeignKey(PsychologistUserProfile, on_delete=models.CASCADE)
