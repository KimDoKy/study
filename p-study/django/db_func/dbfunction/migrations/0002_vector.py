# Generated by Django 2.2 on 2020-02-02 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbfunction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
            ],
        ),
    ]
