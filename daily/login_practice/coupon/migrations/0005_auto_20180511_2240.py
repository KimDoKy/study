# Generated by Django 2.0.4 on 2018-05-11 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0004_auto_20180511_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='use_2_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='use_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
