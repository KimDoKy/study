# Generated by Django 2.0.1 on 2018-03-20 13:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testmodel', '0003_auto_20180319_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testmodel',
            name='gps',
        ),
        migrations.AddField(
            model_name='testmodel',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='lng',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='end_intern',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 18, 13, 59, 42, 840719)),
        ),
    ]