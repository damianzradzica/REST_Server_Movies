# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20170116_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='mail',
            field=models.EmailField(blank=True, max_length=64),
        ),
    ]
