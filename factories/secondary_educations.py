from psychologists.models import PsychologistSecondaryEducation
import factory


class SecondaryEducationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PsychologistSecondaryEducation
        django_get_or_create = ('name', )