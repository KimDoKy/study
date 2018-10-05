# Generated by Django 2.0.2 on 2018-10-05 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
