# Generated by Django 2.0.4 on 2018-05-11 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0003_auto_20180511_2120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='use_date_2nd',
            new_name='use_2_date',
        ),
    ]
