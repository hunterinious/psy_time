from django.core.management.base import BaseCommand
from core.models import WorldCountry
import json


class Command(BaseCommand):
    help = 'Create world countries'

    def handle(self, *args, **kwargs):
        with open('static/files/countries.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        for d in data:
            WorldCountry.objects.create_country_from_json(d)
