from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from factories.locations import CountryWithCitiesFactory


class Command(BaseCommand):
    help = 'Create random countries'

    def add_arguments(self, parser):
        parser.add_argument('countries', type=int, help='Indicates the number of countries to be created')
        parser.add_argument('cities', type=int, help='Indicates the number of countries to be created')

    def handle(self, *args, **kwargs):
        countries = kwargs['countries']
        cities = kwargs['cities']
        CountryWithCitiesFactory.create_batch(size=countries, cities=cities)
