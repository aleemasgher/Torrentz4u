# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-22 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0021_hollywood_youtrailer_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hollywood',
            name='youTrailer_link',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
