from django.db import models
from users.models import PsychologistUser


class PsychologistUserProfile(models.Model):
    birth_date = models.DateField(null=False)
    about = models.TextField(null=False)
    work_experience = models.TextField(null=False)
    price = models.IntegerField(null=False)
    time = models.IntegerField(null=False)
    user = models.OneToOneField(PsychologistUser, on_delete=models.CASCADE)


class PsychologistStatus(models.Model):
    name = models.CharField(unique=True, max_length=50)
    psychologist = models.ManyToManyField(PsychologistUserProfile, related_name="statuses")


class PsychologistWorkFormat(models.Model):
    name = models.CharField(unique=True, max_length=50)
    psychologist = models.ManyToManyField(PsychologistUserProfile, related_name="formats")


class PsychologistTheme(models.Model):
    name = models.CharField(unique=True, max_length=50)
    psychologist = models.ManyToManyField(PsychologistUserProfile, related_name="themes")


class PsychologistApproach(models.Model):
    name = models.CharField(unique=True, max_length=50)
    psychologist = models.ManyToManyField(PsychologistUserProfile, related_name="approaches")


class PsychologistSpecialization(models.Model):
    name = models.CharField(unique=True, max_length=50)
    psychologist = models.ManyToManyField(PsychologistUserProfile, related_name="specializations")


class PsychologistEducation(models.Model):
    name = models.CharField(unique=True, max_length=50)
    psychologist = models.ManyToManyField(PsychologistUserProfile, related_name="educations")


class PsychologistSecondaryEducation(models.Model):
    name = models.CharField(unique=True, max_length=50)
    psychologist = models.ManyToManyField(PsychologistUserProfile, related_name="secondary_educations")


class PsychologistLanguages(models.Model):
    name = models.CharField(unique=True,  max_length=50)
    psychologist = models.ManyToManyField(PsychologistUserProfile, related_name="languages")


class Image(models.Model):
    name = models.CharField(unique=True, max_length=255)
    image = models.ImageField(null=False)
    psychologist = models.ForeignKey(PsychologistUserProfile, on_delete=models.CASCADE)
