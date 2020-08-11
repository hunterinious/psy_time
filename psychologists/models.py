from django.db import models
from users.models import PsychologistUser
from locations.models import City


class PsychologistUserProfile(models.Model):
    avatar = models.ImageField(upload_to="avatars", default="avatars/psy_avatar.jpg")
    birth_date = models.DateField(null=False, blank=False)
    about = models.TextField(null=False, blank=False)
    work_experience = models.TextField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    time = models.IntegerField(null=False, blank=False)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    user = models.OneToOneField(PsychologistUser, on_delete=models.CASCADE)


class PsychologistStatus(models.Model):
    name = models.CharField(unique=True, max_length=50)
    profiles = models.ManyToManyField(PsychologistUserProfile, related_name="statuses")


class PsychologistWorkFormat(models.Model):
    name = models.CharField(unique=True, max_length=50)
    profiles = models.ManyToManyField(PsychologistUserProfile, related_name="formats")


class PsychologistTheme(models.Model):
    name = models.CharField(unique=True, max_length=50)
    profiles = models.ManyToManyField(PsychologistUserProfile, related_name="themes")


class PsychologistApproach(models.Model):
    name = models.CharField(unique=True, max_length=50)
    profiles = models.ManyToManyField(PsychologistUserProfile, related_name="approaches")


class PsychologistSpecialization(models.Model):
    name = models.CharField(unique=True, max_length=50)
    profiles = models.ManyToManyField(PsychologistUserProfile, related_name="specializations")


class PsychologistEducation(models.Model):
    name = models.CharField(unique=True, max_length=50)
    profiles = models.ManyToManyField(PsychologistUserProfile, related_name="educations")


class PsychologistSecondaryEducation(models.Model):
    name = models.CharField(unique=True, max_length=50)
    profiles = models.ManyToManyField(PsychologistUserProfile, related_name="secondary_educations")


class PsychologistLanguages(models.Model):
    name = models.CharField(unique=True, max_length=50)
    profiles = models.ManyToManyField(PsychologistUserProfile, related_name="languages")


class Image(models.Model):
    name = models.CharField(unique=True, max_length=255)
    image = models.ImageField(null=False, blank=False)
    profile = models.ForeignKey(PsychologistUserProfile, on_delete=models.CASCADE)
