# Generated by Django 2.0.5 on 2018-09-01 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180825_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='itinerary_likes',
        ),
    ]
