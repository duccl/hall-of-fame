# Generated by Django 3.0.8 on 2020-07-20 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0002_hall_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='hall',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
    ]
