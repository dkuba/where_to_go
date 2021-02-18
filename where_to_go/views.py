import uuid

from django.http import HttpResponse
from django.shortcuts import render
from places.models import Place, Image

PLACE_URLS = {"легенды": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json",
              "крыши": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/roofs24.json"}


def get_place_details(place: Place) -> dict:
    place_detail_dict = {"title": place.title, "imgs": [],
                       "coordinates": {}}
    place_detail_dict["coordinates"]["lng"] = place.longitude
    place_detail_dict["coordinates"]["lat"] = place.latitude

    for image in place.images.all():
        place_detail_dict["imgs"].append(image.image.url)

    place_detail_dict["description_short"] = place.description_short
    place_detail_dict["description_long"] = place.description_long
    return place_detail_dict


def get_places_info() -> dict:
    places_info_dict = {"type": "FeatureCollection", "features": []}
    for place in Place.objects.all():

        for key in PLACE_URLS:
            if key.upper() in place.title.upper():
                place_url = PLACE_URLS[key]

        feature_dict = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    place.longitude,
                    place.latitude
                ]
            },
            "properties": {
                "title": place.title,
                "placeId": uuid.uuid4(),
                "detailsUrl": place_url
            }
        }
        places_info_dict["features"].append(feature_dict)


    return places_info_dict


def index(request):
    data = {"places_info": get_places_info()}
    return render(request, 'index.html', context=data)
