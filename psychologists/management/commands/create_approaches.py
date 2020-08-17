from django.core.management.base import BaseCommand
from factories.approaches import ApproachFactory


class Command(BaseCommand):
    help = 'Create approaches'

    def handle(self, *args, **kwargs):
        approaches = ('Positive psychotherapy', 'Gestalt approach', 'Psychoanalysis', )
        for a in approaches:
            ApproachFactory.create(name=a)

