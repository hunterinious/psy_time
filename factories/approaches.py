from psychologists.models import PsychologistApproach
import factory


class ApproachFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PsychologistApproach
        django_get_or_create = ('name', )
