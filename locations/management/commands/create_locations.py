from django.core.management.base import BaseCommand
from locations.models import Country


class Command(BaseCommand):
    help = 'Create locations'

    def handle(self, *args, **kwargs):
        with open('static/files/cities_with_timezones.txt', 'r', encoding='utf-8') as file:
            for f in file:
                row = f.split('\t')
                for i, r in enumerate(row):
                    r.strip()
                    row[i] = r.replace('\n', '')

                utc = row[0]
                location = row[1].split('/')
                main_city = location[len(location) - 1]
                country = row[2]

                if len(row) == 4:
                    cities = row[3]
                else:
                    cities = ''

                Country.objects.create_country_with_city_from_file(name=main_city, country_name=country, utc=utc)

