# Generated by Django 2.0.4 on 2018-05-11 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]