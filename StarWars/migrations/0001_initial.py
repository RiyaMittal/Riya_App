# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-18 18:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('episode_id', models.IntegerField(default=0)),
                ('director', models.CharField(max_length=128)),
                ('producer', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Planets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('rotation_period', models.IntegerField()),
                ('orbital_period', models.IntegerField()),
                ('movie_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StarWars.Movies')),
            ],
        ),
    ]