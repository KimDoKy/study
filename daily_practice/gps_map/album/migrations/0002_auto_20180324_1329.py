# Generated by Django 2.0.1 on 2018-03-24 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='lng',
            field=models.FloatField(blank=True, null=True),
        ),
    ]