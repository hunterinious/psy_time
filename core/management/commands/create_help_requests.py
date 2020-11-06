from django.core.management.base import BaseCommand
from factories.help_request import HelpRequestFactory


class Command(BaseCommand):
    help = 'Create help requests'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of help requests to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        HelpRequestFactory.create_batch(size=total)
