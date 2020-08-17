from django.core.management.base import BaseCommand
from factories.statuses import StatusFactory
from random import choice


class Command(BaseCommand):
    help = 'Create statuses'

    def handle(self, *args, **kwargs):
        statuses = ('Psychologist', 'Supervisor', 'Coach', )
        for s in statuses:
            StatusFactory.create(name=s)
