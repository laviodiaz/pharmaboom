# Generated by Django 5.1.1 on 2024-09-22 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharm', '0009_delete_location_remove_pharmacy_latitude_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drug',
            options={'ordering': ['name'], 'verbose_name_plural': 'Лекарственные средства'},
        ),
        migrations.RenameField(
            model_name='drug',
            old_name='drug_name',
            new_name='name',
        ),
    ]