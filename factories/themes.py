from psychologists.models import PsychologistTheme
import factory


class ThemeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PsychologistTheme
        django_get_or_create = ('name', )