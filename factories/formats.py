from psychologists.models import PsychologistWorkFormat
import factory


class FormatFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PsychologistWorkFormat
        django_get_or_create = ('name',)
