from django.core.management.base import BaseCommand
from locations.models import Country
import json


class Command(BaseCommand):
    help = 'Create locations'

    def handle(self, *args, **kwargs):
        with open('static/files/cities_with_timezones.json') as f:
            for obj in json.load(f):
                Country.objects.create_country_with_city_from_file(name=obj['main_city'],
                                                                   country_name=obj['country'],
                                                                   utc=obj['utc'])
