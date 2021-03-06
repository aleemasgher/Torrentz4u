# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-04 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0041_auto_20170905_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Torrents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(blank=True, max_length=350, null=True)),
                ('torrent_size', models.CharField(blank=True, max_length=350, null=True)),
                ('torrent_Link', models.FileField(blank=True, null=True, upload_to='')),
                ('bolly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Bollywood')),
                ('holly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Hollywood')),
            ],
        ),
        migrations.RemoveField(
            model_name='movies',
            name='file_type',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='torrent_Link',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='torrent_size',
        ),
        migrations.AddField(
            model_name='torrents',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movies'),
        ),
    ]
