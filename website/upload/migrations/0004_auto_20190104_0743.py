# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-04 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_uploadedfiles_filehash'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedfiles',
            name='fileName',
        ),
        migrations.AddField(
            model_name='uploadedfiles',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='uploadedfiles',
            name='tags',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='uploadedfiles',
            name='title',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='uploadedfiles',
            name='user',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
