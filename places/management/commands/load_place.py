import os
from urllib.parse import urlparse, unquote

import requests
from django.core.management.base import BaseCommand
from places.models import Place, Image


class Command(BaseCommand):
    help = """Скачивание информации о местах из внешних источников"""

    def add_arguments(self, parser):
        parser.add_argument('place_json_url', type=str)

    def handle(self, *args, **options):

        response = requests.get(url=options['place_json_url'])
        response.raise_for_status()

        decoded_response = response.json()

        place_entity, place_created = Place.objects.get_or_create(
            title=decoded_response['title'],
            defaults={'short_description': decoded_response['description_'
                                                            'short'],
                      'long_description': decoded_response['description_long'],
                      'latitude': decoded_response['coordinates']['lat'],
                      'longitude': decoded_response['coordinates']['lng']}
        )

        if place_created:
            for image_url in decoded_response['imgs']:
                parsed_url = urlparse(image_url)
                new_url = \
                    os.path.join('places',
                                 os.path.basename(unquote(parsed_url.path)))
                Image.objects.create(place=place_entity, image=new_url)
