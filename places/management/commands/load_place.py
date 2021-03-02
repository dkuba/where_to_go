import logging
import os

import requests
from django.core.management.base import BaseCommand
from places.models import Place, Image


class Command(BaseCommand):
    help = """Скачивание информации о местах из внешних источников"""

    def add_arguments(self, parser):
        parser.add_argument('place_json_url', type=str)

    def handle(self, *args, **options):

        try:
            response = requests.get(url=options['place_json_url'])
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            logging.error(err)
            return

        decoded_response = response.json()
        if 'error' in decoded_response:
            logging.error('Сервер вернул ошибку')
            return

        place_entity = Place.objects.get_or_create(
            title=decoded_response['title'],
            defaults={'short_description': decoded_response['description_short'],
                      'long_description': decoded_response['description_long'],
                      'latitude': decoded_response['coordinates']['lat'],
                      'longitude': decoded_response['coordinates']['lng']}
        )

        if place_entity:
            for image_url in decoded_response['imgs']:
                new_url = os.path.join('places', image_url.split('media')[1].replace('/', ''))
                Image.objects.create(place=place_entity[0], image=new_url)
