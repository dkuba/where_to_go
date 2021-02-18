from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from places.models import Place


def get_place_details(place: Place) -> dict:
    place_detail_dict = {'title': place.title, 'imgs': [],
                       'coordinates': {}}
    place_detail_dict['coordinates']['lng'] = place.longitude
    place_detail_dict['coordinates']['lat'] = place.latitude

    for image in place.images.all():
        place_detail_dict['imgs'].append(image.image.url)

    place_detail_dict['description_short'] = place.description_short
    place_detail_dict['description_long'] = place.description_long
    return place_detail_dict


def place(request, place_id):
    place = Place.objects.get(id=place_id)
    return JsonResponse(get_place_details(place))
