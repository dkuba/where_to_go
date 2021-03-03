from django.http import JsonResponse

from places.models import Place


def get_place_details(place: Place):
    place_detail = {'title': place.title, 'imgs': [],
                    'description_short': place.short_description,
                    'description_long': place.long_description,
                    'coordinates': {'lng': place.longitude,
                                    'lat': place.latitude}, }

    for image in place.images.all():
        place_detail['imgs'].append(image.image.url)

    return place_detail


def get_place(request, place_id):
    place = Place.objects.get(id=place_id)
    return JsonResponse(get_place_details(place),
                        json_dumps_params={'indent': 2,
                                           'ensure_ascii': False})
