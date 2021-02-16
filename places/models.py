from django.db import models


class Place(models.Model):
    """Место"""

    title = models.CharField("Наименование", max_length=50)
    description_short = models.TextField("Краткое описание")
    description_long = models.TextField("Полное описание")
    latitude = models.FloatField("Широта")
    longitude = models.FloatField("Долгота")

    def __str__(self):
        return self.title
