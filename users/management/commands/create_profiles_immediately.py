from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from factories.users_and_profiles import (
    UserFactory,
    RegularUserProfileFactory,
    PsychologistUserProfileFactory,
)
from factories.approaches import ApproachFactory
from factories.educations import EducationFactory
from factories.formats import FormatFactory
from factories.languages import LanguageFactory
from factories.secondary_educations import SecondaryEducationFactory
from factories.specializations import SpecializationFactory
from factories.statuses import StatusFactory
from factories.themes import ThemeFactory
from factories.locations import CountryWithCitiesFactory
from factories.psy_reviews import PsychologistReviewFactory
from random import choice, sample


User = get_user_model()


class Command(BaseCommand):
    help = 'Create users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of profiles to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']

        approaches = ('Positive psychotherapy', 'Gestalt approach', 'Psychoanalysis',)
        educations = ('Psychologist', 'Social psychologist', 'Medical psychologist', 'Clinical psychologist')
        secondary_educations = ('Marketer', 'Financier', 'Lawyer', 'Developer',)
        formats = ('Individual counseling', 'Working with pairs',)
        languages = ('Ukrainian', 'Russian', 'English',)
        specializations = ('Gestalt approach in working with couples', 'Sexology', 'Family therapy',
                           'Developmental crises', 'Crises and trauma',
                           'Gestalt therapy and organizational coaching',)
        statuses = ('Psychologist', 'Supervisor', 'Coach',)
        themes = ('Psychosomatics', 'Depression', 'Self-esteem, self-acceptance', 'Loneliness, socialization',
                  'Vocational guidance',)

        approaches = [ApproachFactory.create(name=a) for a in approaches]
        educations = [EducationFactory.create(name=e) for e in educations]
        secondary_educations = [SecondaryEducationFactory.create(name=se) for se in secondary_educations]
        formats = [FormatFactory.create(name=f) for f in formats]
        languages = [LanguageFactory.create(name=l) for l in languages]
        specializations = [SpecializationFactory.create(name=s) for s in specializations]
        statuses = [StatusFactory.create(name=s) for s in statuses]
        themes = [ThemeFactory.create(name=t) for t in themes]

        users = UserFactory.create_batch(size=total)
        countries = CountryWithCitiesFactory.create_batch(size=total, cities=4)
        cities = [c.cities.all() for c in countries]

        psychologist_users = []
        regular_users = []
        for u in users:
            if u.user_type == User.UserTypes.PSYCHOLOGIST_USER:
                city = choice(choice(cities))
                r_statuses = sample(statuses, k=len(statuses) - 1)
                r_formats = sample(formats, k=len(formats) - 1)
                r_themes = sample(themes, k=len(themes) - 2)
                r_approaches = sample(approaches, k=len(approaches) - 2)
                r_specializations = sample(specializations, k=1)
                r_educations = sample(educations, k=1)
                r_secondary_educations = sample(secondary_educations, k=len(secondary_educations) - 2)
                r_languages = sample(languages, k=len(languages) - 1)

                PsychologistUserProfileFactory.create(user=u,
                                                      city=city,
                                                      statuses=r_statuses,
                                                      formats=r_formats,
                                                      themes=r_themes,
                                                      approaches=r_approaches,
                                                      languages=r_languages,
                                                      specializations=r_specializations,
                                                      educations=r_educations,
                                                      secondary_educations=r_secondary_educations)
                psychologist_users.append(u)
            elif u.user_type == User.UserTypes.REGULAR_USER:
                RegularUserProfileFactory.create(user=u)
                regular_users.append(u)

        for _ in users:
            psy_user = choice(psychologist_users)
            regular_user = choice(regular_users)
            PsychologistReviewFactory.create(author=regular_user, psychologist=psy_user)


