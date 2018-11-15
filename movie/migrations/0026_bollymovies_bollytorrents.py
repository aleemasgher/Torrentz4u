# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-26 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0025_auto_20170823_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='BollyMovies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=250)),
                ('movie_year', models.CharField(max_length=4)),
                ('country', models.CharField(max_length=500)),
                ('movie_rating', models.CharField(max_length=10, null=True)),
                ('description', models.TextField()),
                ('cast', models.CharField(max_length=100)),
                ('movie_logo', models.FileField(upload_to='')),
                ('youTrailer_link', models.CharField(max_length=10000, null=True)),
                ('publish', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created', '-update'],
            },
        ),
        migrations.CreateModel(
            name='BollyTorrents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(blank=True, max_length=350, null=True)),
                ('torrent_size', models.CharField(blank=True, max_length=350, null=True)),
                ('torrent_Link', models.FileField(blank=True, null=True, upload_to='')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movies')),
            ],
        ),
    ]
