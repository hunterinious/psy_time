from random import choice
from datetime import date
from django.db import models
from django.db.models import Count, Min, Max
from django.utils.translation import gettext_lazy as _
from users.models import RegularUser, PsychologistUser
from locations.models import City


class PsychologistStatusManager(models.Manager):
    def get_statuses(self):
        return self.all()


class PsychologistStatus(models.Model):
    name = models.CharField(unique=True, max_length=50)

    objects = PsychologistStatusManager()

    def __str__(self):
        return self.name


class PsychologistWorkFormatManager(models.Manager):
    def get_formats(self):
        return self.all()


class PsychologistWorkFormat(models.Model):
    name = models.CharField(unique=True, max_length=50)

    objects = PsychologistWorkFormatManager()

    def __str__(self):
        return self.name


class PsychologistThemeManager(models.Manager):
    def get_themes(self):
        return self.all()


class PsychologistTheme(models.Model):
    name = models.CharField(unique=True, max_length=50)

    objects = PsychologistThemeManager()

    def __str__(self):
        return self.name


class PsychologistApproachManager(models.Manager):
    def get_approaches(self):
        return self.all()


class PsychologistApproach(models.Model):
    name = models.CharField(unique=True, max_length=50)

    objects = PsychologistApproachManager()

    def __str__(self):
        return self.name


class PsychologistSpecializationManager(models.Manager):
    def get_specializations(self):
        return self.all()


class PsychologistSpecialization(models.Model):
    name = models.CharField(unique=True, max_length=50)

    objects = PsychologistSpecializationManager()

    def __str__(self):
        return self.name


class PsychologistEducationManager(models.Manager):
    def get_educations(self):
        return self.all()


class PsychologistEducation(models.Model):
    name = models.CharField(unique=True, max_length=50)

    objects = PsychologistEducationManager()

    def __str__(self):
        return self.name


class PsychologistSecondaryEducationManager(models.Manager):
    def get_secondary_educations(self):
        return self.all()


class PsychologistSecondaryEducation(models.Model):
    name = models.CharField(unique=True, max_length=50)

    objects = PsychologistSecondaryEducationManager()

    def __str__(self):
        return self.name


class PsychologistLanguageManager(models.Manager):
    def get_languages(self):
        return self.all()


class PsychologistLanguage(models.Model):
    name = models.CharField(unique=True, max_length=50)

    objects = PsychologistLanguageManager()

    def __str__(self):
        return self.name


class PsychologistUserProfileManager(models.Manager):
    def get_min_age(self):
        min_age = self.all().aggregate(Max('birth_date__year'))
        current_year = date.today().year
        return current_year - min_age['birth_date__year__max'].year

    def get_max_age(self):
        max_age = self.all().aggregate(Min('birth_date__year'))
        current_year = date.today().year
        return current_year - max_age['birth_date__year__min'].year

    def get_genders(self):
        return self.model.Gender.labels

    def get_profiles(self):
        return self.all()

    def get_random_profile(self):
        return choice(self.all())

    def get_profiles_by_criteria(self, age, genders, statuses, formats, themes, approaches,
                                 specializations, educations, secondary_educations, languages):

        profiles = self.get_profiles()

        if genders:
            gender = genders[0]
            if gender == 'Male':
                gender = self.model.Gender.MALE.value
            else:
                gender = self.model.Gender.FEMALE.value
            profiles = profiles.filter(gender=gender)
        if age:
            current_year = date.today().year
            age_min = age[0]
            age_max = age[1]
            profiles = profiles.filter(
                birth_date__year__range=(current_year - age_max, current_year - age_min))
        if statuses:
            profiles = profiles.filter(statuses__name__in=statuses).annotate(
                st=Count('statuses__name', distinct=True)).filter(st__gte=len(statuses))
        if formats:
            profiles = profiles.filter(formats__name__in=formats).annotate(
                st=Count('formats__name', distinct=True)).filter(st=len(formats))
        if themes:
            profiles = profiles.filter(themes__name__in=themes).annotate(
                st=Count('themes__name', distinct=True)).filter(st=len(themes))
        if approaches:
            profiles = profiles.filter(approaches__name__in=approaches).annotate(
                st=Count('approaches__name', distinct=True)).filter(st=len(approaches))
        if specializations:
            profiles = profiles.filter(specializations__name__in=specializations).annotate(
                st=Count('specializations__name', distinct=True)).filter(st=len(specializations))
        if educations:
            profiles = profiles.filter(educations__name__in=educations).annotate(
                st=Count('educations__name', distinct=True)).filter(st=len(educations))
        if secondary_educations:
            profiles = profiles.filter(secondary_educations__name__in=secondary_educations).annotate(
                st=Count('secondary_educations__name', distinct=True)).filter(st=len(secondary_educations))
        if languages:
            profiles = profiles.filter(languages__name__in=languages).annotate(
                l=Count('languages__name', distinct=True)).filter(l__gte=len(languages))

        return profiles


class PsychologistUserProfile(models.Model):

    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')

    objects = PsychologistUserProfileManager()

    gender = models.CharField(max_length=50, choices=Gender.choices)
    avatar = models.ImageField(null=False, blank=False, default="avatars/psy_avatar.jpg", upload_to='avatars')
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

    def __str__(self):
        return str(self.user)


class PsychologistReview(models.Model):
    text = models.TextField()
    author = models.ForeignKey(RegularUser, related_name="reviews", on_delete=models.CASCADE)
    psychologist = models.ForeignKey(PsychologistUser, related_name="psy_reviews", on_delete=models.CASCADE)


class Image(models.Model):
    name = models.CharField(unique=True, max_length=255)
    image = models.ImageField(null=False, blank=False)
    profile = models.ForeignKey(PsychologistUserProfile, on_delete=models.CASCADE)
