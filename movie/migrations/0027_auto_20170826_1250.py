# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-26 07:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0026_bollymovies_bollytorrents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bollytorrents',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.BollyMovies'),
        ),
    ]
