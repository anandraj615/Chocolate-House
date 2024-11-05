# Generated by Django 5.1.2 on 2024-11-05 12:01

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerSuggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('flavour_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('allergies', models.TextField(blank=True, help_text='Any Concernson ')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('quantity', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('unit', models.CharField(max_length=20)),
                ('allergen', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='Flavour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('ingredients', models.ManyToManyField(related_name='flavors', to='myapp.ingredient')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.season')),
            ],
        ),
    ]
