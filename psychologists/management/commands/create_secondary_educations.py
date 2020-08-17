from django.core.management.base import BaseCommand
from factories.secondary_educations import SecondaryEducationFactory


class Command(BaseCommand):
    help = 'Create secondary educations'

    def handle(self, *args, **kwargs):
        secondary_educations = ('Marketer', 'Financier', 'Lawyer', 'Developer', )
        for se in secondary_educations:
            SecondaryEducationFactory.create(name=se)
