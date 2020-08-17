from psychologists.models import PsychologistStatus
import factory


class StatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PsychologistStatus
        django_get_or_create = ('name', )