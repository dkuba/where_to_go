import os

import requests
from django.core.management.base import BaseCommand
from places.models import Place, Image


class Command(BaseCommand):
    help = """Скачивание информации о местах из внешних источников"""

    def add_arguments(self, parser):
        parser.add_argument('place_json_url', type=str)

    def handle(self, *args, **options):
        resp = requests.get(url=options['place_json_url'])
        data = resp.json()
        Place.objects.get_or_create(
            title=data['title'],
            description_short=data['description_short'],
            description_long=data['description_long'],
            latitude=data['coordinates']['lat'],
            longitude=data['coordinates']['lng'],
        )
        place = list(Place.objects.all())[-1]
        for image_url in data['imgs']:
            new_url = os.path.join('places', image_url.split('media')[1].replace('/', ''))
            Image.objects.create(place=place, image=new_url)
