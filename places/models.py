from django.db import models
from tinymce.models import HTMLField


def image_number_default(obj):
    return obj.count()


class Place(models.Model):
    """Место"""

    title = models.CharField('Наименование', max_length=50)

    description_short = models.TextField('Краткое описание')
    description_long = HTMLField('Полное описание')
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    def __str__(self):
        return self.title

    class Meta(object):
        verbose_name = "Место"
        verbose_name_plural = "Места"


class Image(models.Model):
    """Картинки"""

    @staticmethod
    def get_next_item_number():
        return Image.objects.count() + 1

    place = models.ForeignKey(Place, verbose_name='Место',
                              related_name='images',
                              on_delete=models.CASCADE, default=None)
    image = models.ImageField('Картинка',
                              upload_to='places', null=True, blank=True)
    number = models.PositiveBigIntegerField(
        'Порядковый номер', null=False,
        blank=False, default=get_next_item_number.__func__)

    class Meta(object):
        ordering = ['number']
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return f'{self.number} {self.place}'
