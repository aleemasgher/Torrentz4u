# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-04 19:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0039_auto_20170904_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='hollywood',
            name='torrent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.Torrents'),
        ),
    ]
