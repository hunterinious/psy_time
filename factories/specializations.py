from psychologists.models import PsychologistSpecialization
import factory


class SpecializationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PsychologistSpecialization
        django_get_or_create = ('name', )