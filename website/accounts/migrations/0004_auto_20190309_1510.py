# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-09 09:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
