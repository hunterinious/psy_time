from psychologists.models import PsychologistLanguage
import factory


class LanguageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PsychologistLanguage
        django_get_or_create = ('name', )

    name = factory.Faker('language')
