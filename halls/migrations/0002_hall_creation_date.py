# Generated by Django 3.0.8 on 2020-07-19 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hall',
            name='creation_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
