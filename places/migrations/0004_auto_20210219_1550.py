# Generated by Django 3.1.6 on 2021-02-19 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20210219_1548'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['number'], 'verbose_name': 'Картинка',
                     'verbose_name_plural': 'Картинки'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
    ]
