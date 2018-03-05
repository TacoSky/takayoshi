# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-04 22:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('takayoshi', '0004_classification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('achievement', models.CharField(blank=True, max_length=256)),
                ('order', models.IntegerField(blank=True)),
                ('image', models.CharField(max_length=256)),
                ('url', models.CharField(blank=True, max_length=256)),
                ('description', models.CharField(blank=True, max_length=1024)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='takayoshi.Company')),
            ],
        ),
    ]