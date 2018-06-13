# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-04 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0036_auto_20170904_1247'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BollyTorrents',
            new_name='Torrents',
        ),
        migrations.RemoveField(
            model_name='bollydetail',
            name='bolly',
        ),
        migrations.RemoveField(
            model_name='hollydetail',
            name='holly',
        ),
        migrations.RemoveField(
            model_name='hollytorrents',
            name='movie',
        ),
        migrations.AddField(
            model_name='movies',
            name='cast',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='movies',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='movies',
            name='movie_rating',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='movies',
            name='youTrailer_link',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='torrents',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movies'),
        ),
        migrations.DeleteModel(
            name='BollyDetail',
        ),
        migrations.DeleteModel(
            name='HollyDetail',
        ),
        migrations.DeleteModel(
            name='HollyTorrents',
        ),
    ]