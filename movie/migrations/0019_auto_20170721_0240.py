# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-20 21:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0018_auto_20170721_0236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hollywood',
            name='created',
        ),
        migrations.RemoveField(
            model_name='hollywood',
            name='updated',
        ),
    ]
