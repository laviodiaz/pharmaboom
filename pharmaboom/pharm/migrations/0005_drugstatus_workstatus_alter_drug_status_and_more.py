# Generated by Django 5.1.1 on 2024-09-15 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharm', '0004_alter_city_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrugStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_status', models.CharField(max_length=25, verbose_name='Статус наличия товара')),
            ],
            options={
                'verbose_name_plural': 'Статусы наличия',
                'ordering': ['drug_status'],
            },
        ),
        migrations.CreateModel(
            name='WorkStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_status', models.CharField(max_length=25, verbose_name='Статус работы аптеки/апт.сети')),
            ],
            options={
                'verbose_name_plural': 'Статусы работы',
                'ordering': ['work_status'],
            },
        ),
        migrations.AlterField(
            model_name='drug',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pharm.drugstatus'),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pharm.workstatus'),
        ),
        migrations.AlterField(
            model_name='pharmchain',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pharm.workstatus'),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
