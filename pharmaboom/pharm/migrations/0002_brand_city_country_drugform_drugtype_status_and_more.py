# Generated by Django 5.1.1 on 2024-09-15 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=50, verbose_name='Название бренда')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=25, verbose_name='Город')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counry_name', models.CharField(max_length=50, verbose_name='Страна')),
            ],
        ),
        migrations.CreateModel(
            name='DrugForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_name', models.CharField(max_length=50, verbose_name='Лекарственная форма')),
            ],
        ),
        migrations.CreateModel(
            name='DrugType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_type', models.CharField(max_length=50, verbose_name='Форма отпуска')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_status', models.CharField(max_length=25, verbose_name='Статус')),
            ],
        ),
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='corp',
        ),
        migrations.RemoveField(
            model_name='product',
            name='drug_form',
        ),
        migrations.RemoveField(
            model_name='product',
            name='drug_type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pharm.city'),
        ),
        migrations.AlterField(
            model_name='pharmchain',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pharm.city'),
        ),
        migrations.CreateModel(
            name='Corporation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corp_name', models.CharField(max_length=50, verbose_name='Наименование производителя')),
                ('corp_country', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pharm.country')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pharm.country'),
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_name', models.CharField(max_length=50, verbose_name='Наименование препарата')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена товара, сом')),
                ('amount', models.IntegerField(verbose_name='Количество')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pharm.brand')),
                ('corp', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pharm.corporation')),
                ('drug_form', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pharm.drugform')),
                ('drug_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pharm.drugtype')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pharm.status')),
            ],
            options={
                'verbose_name_plural': 'Товары',
                'ordering': ['drug_name'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='drug',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='pharm.drug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pharm.status'),
        ),
        migrations.AlterField(
            model_name='pharmchain',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pharm.status'),
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
    ]