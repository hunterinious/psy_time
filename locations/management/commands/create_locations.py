from django.core.management.base import BaseCommand
from factories.locations import CountryWithCitiesFactory


class Command(BaseCommand):
    help = 'Create locations'

    def handle(self, *args, **kwargs):
        countries = kwargs['countries']
        cities = kwargs['cities']
        CountryWithCitiesFactory.create_batch(size=countries, cities=cities)
