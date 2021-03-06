# Generated by Django 3.1.6 on 2021-02-20 07:10

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20210219_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='number',
            field=models.PositiveBigIntegerField(default=0,
                                                 verbose_name='Порядковый '
                                                              'номер'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(verbose_name='Полное описание'),
        ),
    ]
