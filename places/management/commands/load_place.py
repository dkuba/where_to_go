import os

import requests
from django.core.management.base import BaseCommand
from places.models import Place, Image


class Command(BaseCommand):
    help = """Скачивание информации о местах из внешних источников"""

    def add_arguments(self, parser):
        parser.add_argument('place_json_url', type=str)

    def handle(self, *args, **options):
        place = requests.get(url=options['place_json_url']).json()
        place = Place.objects.get_or_create(
            title=place['title'],
            defaults={'description_short': place['description_short'],
                      'description_long': place['description_long'],
                      'latitude': place['coordinates']['lat'],
                      'longitude': place['coordinates']['lng']}
        )
        for image_url in place['imgs']:
            new_url = os.path.join('places', image_url.split('media')[1].replace('/', ''))
            Image.objects.create(place=place, image=new_url)
