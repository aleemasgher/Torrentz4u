# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 20:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0034_movie'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
