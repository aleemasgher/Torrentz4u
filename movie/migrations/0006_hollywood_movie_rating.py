# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-20 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_remove_hollywood_ss'),
    ]

    operations = [
        migrations.AddField(
            model_name='hollywood',
            name='movie_rating',
            field=models.CharField(max_length=10, null=True),
        ),
    ]