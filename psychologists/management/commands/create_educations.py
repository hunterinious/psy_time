from django.core.management.base import BaseCommand
from factories.educations import EducationFactory


class Command(BaseCommand):
    help = 'Create approaches'

    def handle(self, *args, **kwargs):
        educations = ('Psychologist', 'Social psychologist', 'Medical psychologist', 'Clinical psychologist')
        for e in educations:
            EducationFactory.create(name=e)
