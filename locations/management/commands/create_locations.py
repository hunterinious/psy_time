from django.core.management.base import BaseCommand
from locations.models import Country, City
import json


class Command(BaseCommand):
    help = 'Create locations'

    def handle(self, *args, **kwargs):
        with open('static/files/countries.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        for d in data:
            Country.objects.create_country_from_json(d)
