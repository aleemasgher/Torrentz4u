# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-26 19:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0032_bollymovies_bollytorrents'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bollytorrents',
            name='movie',
        ),
        migrations.DeleteModel(
            name='BollyMovies',
        ),
        migrations.DeleteModel(
            name='BollyTorrents',
        ),
    ]
