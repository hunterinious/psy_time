from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from factories.users_and_profiles import RegularUserProfileFactory, PsychologistUserProfileFactory
from locations.models import City
from psychologists.models import (
    PsychologistTheme,
    PsychologistStatus,
    PsychologistSpecialization,
    PsychologistEducation,
    PsychologistSecondaryEducation,
    PsychologistLanguage,
    PsychologistWorkFormat,
    PsychologistApproach,
)
from random import choice, sample

User = get_user_model()


class Command(BaseCommand):
    help = 'Create users'

    def handle(self, *args, **kwargs):
        objects = User.objects
        users = list(objects.all())
        cities = list(City.objects.all())
        statuses = list(PsychologistStatus.objects.all())
        formats = list(PsychologistWorkFormat.objects.all())
        themes = list(PsychologistTheme.objects.all())
        approaches = list(PsychologistApproach.objects.all())
        specializations = list(PsychologistSpecialization.objects.all())
        educations = list(PsychologistEducation.objects.all())
        secondary_educations = list(PsychologistSecondaryEducation.objects.all())
        languages = list(PsychologistLanguage.objects.all())

        for u in users:
            if u.user_type == User.UserTypes.PSYCHOLOGIST_USER:
                city = choice(cities)
                r_statuses = sample(statuses, k=len(statuses) - 1)
                r_formats = sample(formats, k=len(formats) - 1)
                r_themes = sample(themes, k=len(themes) - 2)
                r_approaches = sample(approaches, k=len(approaches) - 2)
                r_specializations = sample(specializations, k=1)
                r_educations = sample(educations, k=1)
                r_secondary_educations = sample(secondary_educations, k=len(secondary_educations) - 2)
                r_languages = sample(languages, k=len(languages) - 1)

                PsychologistUserProfileFactory.create(user=u, city=city, statuses=r_statuses, formats=r_formats,
                                                      themes=r_themes, approaches=r_approaches, languages=r_languages,
                                                      specializations=r_specializations, educations=r_educations,
                                                      secondary_educations=r_secondary_educations)
            elif u.user_type == User.UserTypes.REGULAR_USER:
                RegularUserProfileFactory.create(user=u)

