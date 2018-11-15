# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-04 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0038_auto_20170904_2314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bollywood',
            options={'ordering': ['-created', '-update']},
        ),
        migrations.AlterModelOptions(
            name='hollywood',
            options={'ordering': ['-created', '-update']},
        ),
        migrations.AddField(
            model_name='bollywood',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='bollywood',
            name='update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='hollywood',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='hollywood',
            name='update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
