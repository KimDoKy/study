# Generated by Django 2.2 on 2020-01-31 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlog',
            name='is_cancle',
            field=models.BooleanField(default=False),
        ),
    ]