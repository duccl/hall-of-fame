# Generated by Django 3.0.8 on 2020-07-21 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0003_hall_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='url',
            field=models.URLField(default=''),
        ),
    ]
