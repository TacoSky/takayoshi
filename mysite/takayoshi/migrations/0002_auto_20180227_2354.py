# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-28 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('takayoshi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='order',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='order',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='joberole',
            name='order',
            field=models.IntegerField(blank=True),
        ),
    ]