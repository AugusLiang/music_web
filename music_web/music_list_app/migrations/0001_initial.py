# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-28 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('singer', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=50)),
                ('lyric', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SongType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='song_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='music_list_app.SongType'),
        ),
    ]
