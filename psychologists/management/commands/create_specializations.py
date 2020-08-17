from django.core.management.base import BaseCommand
from factories.specializations import SpecializationFactory


class Command(BaseCommand):
    help = 'Create statuses'

    def handle(self, *args, **kwargs):
        specializations = ('Gestalt approach in working with couples', 'Sexology', 'Family therapy',
                           'Developmental crises', 'Crises and trauma',
                           'Gestalt therapy and organizational coaching', )
        for s in specializations:
            SpecializationFactory.create(name=s)
