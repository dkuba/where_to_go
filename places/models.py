from django.db import models
from tinymce.models import HTMLField


def image_number_default(obj):
    return obj.count()


class Place(models.Model):
    """Место"""

    title = models.CharField('Наименование', max_length=50)

    short_description = models.TextField('Краткое описание', null=True, blank=True)
    long_description = HTMLField('Полное описание', null=True, blank=True)
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    def __str__(self):
        return self.title

    class Meta(object):
        verbose_name = "Место"
        verbose_name_plural = "Места"


class Image(models.Model):
    """Картинки"""

    place = models.ForeignKey(Place, verbose_name='Место',
                              related_name='images',
                              on_delete=models.CASCADE)
    image = models.ImageField('Картинка', upload_to='places')
    number = models.PositiveBigIntegerField(
        'Порядковый номер', default=0, null=True, blank=True)

    class Meta(object):
        ordering = ['number']
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return f'{self.number} {self.place}'
