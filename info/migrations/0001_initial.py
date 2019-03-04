# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-04 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=32, verbose_name='账户')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('phone', models.CharField(max_length=32, verbose_name='手机号')),
                ('qq', models.CharField(max_length=32, verbose_name='qq')),
                ('email', models.CharField(max_length=32, verbose_name='邮箱')),
                ('wechat', models.CharField(max_length=32, verbose_name='微信')),
            ],
        ),
    ]