# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-07 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account',
            field=models.CharField(max_length=32, unique=True, verbose_name='账户'),
        ),
    ]
