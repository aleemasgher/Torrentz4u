# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-26 08:21
from __future__ import unicode_literals

from django.db import migrations, models
import movie.models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0028_auto_20170826_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torrents',
            name='movie',
            field=models.ForeignKey(on_delete=movie.models.Movies, to='movie.Movies'),
        ),
    ]