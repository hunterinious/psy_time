from django.core.management.base import BaseCommand
from factories.users_and_profiles import UserFactory


class Command(BaseCommand):
    help = 'Create users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        UserFactory.create_batch(size=total)

