from django.core.management.base import BaseCommand
from factories.themes import ThemeFactory


class Command(BaseCommand):
    help = 'Create themes'

    def handle(self, *args, **kwargs):
        themes = ('Psychosomatics', 'Depression', 'Self-esteem, self-acceptance', 'Loneliness, socialization',
                  'Vocational guidance', )
        for t in themes:
            ThemeFactory.create(name=t)
