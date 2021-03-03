from django.shortcuts import render
from django.urls import reverse

from places.models import Place


def get_geojson_formatted_places():
    places = {'type': 'FeatureCollection', 'features': []}

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
                'detailsUrl': reverse('place', args=(place.id,))
            }
        }
        places['features'].append(feature_dict)

    return places


def index(request):
    return render(request, 'index.html',
                  context={'geojson_formatted_places':
                           get_geojson_formatted_places()})
