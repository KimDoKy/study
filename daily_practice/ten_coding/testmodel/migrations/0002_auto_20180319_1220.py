# Generated by Django 2.0.1 on 2018-03-19 12:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testmodel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='end_intern',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 17, 12, 20, 6, 185827)),
        ),
    ]
