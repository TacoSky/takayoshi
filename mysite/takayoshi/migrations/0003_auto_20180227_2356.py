# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-28 04:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('takayoshi', '0002_auto_20180227_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='url',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
