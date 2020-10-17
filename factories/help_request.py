from random import randint
from core.models import Help
from factory.faker import faker
import factory.fuzzy
import factory

fake = faker.Faker()


class HelpRequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Help
        django_get_or_create = ('email', 'username')

    email = factory.Sequence(lambda e: 'user{}@gmail.com'.format(e))
    username = factory.Sequence(lambda u: '{}'.format(fake.name()))
    country = factory.Faker('country')
    theme = factory.fuzzy.FuzzyText(length=12)
    message = factory.Faker('text')

    @factory.lazy_attribute
    def status(self):
        rand_value = randint(0, 120)

        if rand_value < 50:
            user_type = Help.Status.PENDING
        elif rand_value < 100:
            user_type = Help.Status.IN_PROCESS
        else:
            user_type = Help.Status.CLOSED

        return user_type
