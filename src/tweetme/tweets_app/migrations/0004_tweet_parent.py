# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-03 16:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets_app', '0003_auto_20181101_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tweets_app.Tweet'),
        ),
    ]
