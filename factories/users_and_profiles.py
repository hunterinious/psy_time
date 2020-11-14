from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from users.models import RegularUserProfile
from psychologists.models import PsychologistUserProfile
from .locations import CityFactory
from random import randint
from factory.faker import faker
import factory


User = get_user_model()
fake = faker.Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('email', )

    email = factory.Sequence(lambda e: 'user{}@gmail.com'.format(e))
    password = factory.Sequence(lambda p: make_password('password1234{}'.format(p)))

    @factory.lazy_attribute
    def user_type(self):
        rand_value = randint(0, 120)

        if rand_value < 50:
            user_type = User.UserTypes.REGULAR_USER
        elif rand_value < 100:
            user_type = User.UserTypes.PSYCHOLOGIST_USER
        else:
            user_type = User.UserTypes.ADMIN_USER

        return user_type


class RegularUserProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RegularUserProfile

    name = factory.Faker('name')
    avatar = factory.Faker('name')
    city = factory.SubFactory(CityFactory)
    user = factory.SubFactory(UserFactory, user_type=User.UserTypes.REGULAR_USER)


class PsychologistUserProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PsychologistUserProfile

    name = factory.Faker('name')
    about = factory.Faker('paragraph')
    work_experience = factory.Faker('paragraph')
    birth_date = factory.Faker('date_of_birth')
    price = randint(50, 100)
    duration = randint(50, 60)
    city = factory.SubFactory(CityFactory)
    user = factory.SubFactory(UserFactory, user_type=User.UserTypes.PSYCHOLOGIST_USER)

    @factory.lazy_attribute
    def gender(self):
        rand_value = randint(0, 1)

        if rand_value == 0:
            gender = PsychologistUserProfile.Gender.FEMALE
        elif rand_value == 1:
            gender = PsychologistUserProfile.Gender.MALE

        return gender

    @factory.post_generation
    def statuses(self, create, extracted):
        if not create:
            return
        if extracted:
            for status in extracted:
                self.statuses.add(status)

    @factory.post_generation
    def formats(self, create, extracted):
        if not create:
            return
        if extracted:
            for format in extracted:
                self.formats.add(format)

    @factory.post_generation
    def themes(self, create, extracted):
        if not create:
            return
        if extracted:
            for theme in extracted:
                self.themes.add(theme)

    @factory.post_generation
    def approaches(self, create, extracted):
        if not create:
            return
        if extracted:
            for approach in extracted:
                self.approaches.add(approach)

    @factory.post_generation
    def languages(self, create, extracted):
        if not create:
            return
        if extracted:
            for language in extracted:
                self.languages.add(language)

    @factory.post_generation
    def specializations(self, create, extracted):
        if not create:
            return
        if extracted:
            for specialization in extracted:
                self.specializations.add(specialization)

    @factory.post_generation
    def educations(self, create, extracted):
        if not create:
            return
        if extracted:
            for education in extracted:
                self.educations.add(education)

    @factory.post_generation
    def secondary_educations(self, create, extracted):
        if not create:
            return
        if extracted:
            for secondary_education in extracted:
                self.secondary_educations.add(secondary_education)
