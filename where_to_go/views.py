import uuid

from django.http import HttpResponse
from django.shortcuts import render
from places.models import Place


def get_places_info():
    places_info = {'type': 'FeatureCollection', 'features': []}

    for place in Place.objects.all():
        feature_dict = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [
                    place.longitude,
                    place.latitude
                ]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': f'places/{place.id}'
            }
        }
        places_info['features'].append(feature_dict)

    return places_info


def index(request):
    return render(request, 'index.html', context={'places_info': get_places_info()})
