from django.core.management.base import BaseCommand
from factories.formats import FormatFactory


class Command(BaseCommand):
    help = 'Create formats'

    def handle(self, *args, **kwargs):
        formats = ('Individual counseling', 'Working with pairs', )
        for f in formats:
            FormatFactory.create(name=f)

