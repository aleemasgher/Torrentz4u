# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-20 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20170720_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='hollywood',
            name='photo',
            field=models.ImageField(null=True, upload_to='ScreenShots'),
        ),
    ]