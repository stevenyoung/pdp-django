# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-17 22:42
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coords', django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326)),
            ],
        ),
    ]
