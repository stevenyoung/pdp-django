# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20170513_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='scene',
            name='name',
            field=models.TextField(default=''),
        ),
    ]