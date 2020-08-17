from django.core.management.base import BaseCommand
from factories.languages import LanguageFactory


class Command(BaseCommand):
    help = 'Create languages'

    def handle(self, *args, **kwargs):
        languages = ('Ukrainian', 'Russian', 'English', )
        for l in languages:
            LanguageFactory.create(name=l)
