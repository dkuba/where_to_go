from django.db import models


class Place(models.Model):
    """Место"""

    title = models.CharField('Наименование', max_length=50)
    description_short = models.TextField('Краткое описание')
    description_long = models.TextField('Полное описание')
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    """Картинки"""

    place = models.ForeignKey(Place, verbose_name='Место',
                              related_name='images',
                              on_delete=models.CASCADE, default=None)
    image = models.ImageField('Картинка',
                              upload_to='places', null=True, blank=True)
    number = models.IntegerField("Порядковый номер")

    def __str__(self):
        return f'{self.number} {self.place}'
