# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-18 05:31
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='video',
            field=models.URLField(max_length=256, null=True, verbose_name='video'),
        ),
        migrations.AlterField(
            model_name='contentitem',
            name='list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, max_length=32, null=True), size=16),
        ),
    ]
