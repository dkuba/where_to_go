# Generated by Django 3.1.6 on 2021-02-19 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20210217_1725'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['number']},
        ),
        migrations.AlterField(
            model_name='image',
            name='number',
            field=models.PositiveBigIntegerField(verbose_name='Порядковый номер'),
        ),
    ]
