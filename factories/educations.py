from psychologists.models import PsychologistEducation
import factory


class EducationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PsychologistEducation
        django_get_or_create = ('name', )
