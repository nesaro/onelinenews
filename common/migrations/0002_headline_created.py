# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 18:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='headline',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
