# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-19 00:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20170518_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='first_name',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='artist',
            name='last_name',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Artist'),
        ),
    ]
