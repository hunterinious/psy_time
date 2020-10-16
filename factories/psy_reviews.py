from psychologists.models import PsychologistReview
import factory


class PsychologistReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PsychologistReview

    text = factory.Faker('paragraph')
