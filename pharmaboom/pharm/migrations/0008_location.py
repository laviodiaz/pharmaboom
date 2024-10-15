# Generated by Django 5.1.1 on 2024-09-22 13:04

import django_admin_geomap
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharm', '0007_alter_corporation_options_alter_pharmacy_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            bases=(models.Model, django_admin_geomap.GeoItem),
        ),
    ]
