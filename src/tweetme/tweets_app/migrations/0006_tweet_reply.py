# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-07 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets_app', '0005_tweet_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='reply',
            field=models.BooleanField(default=False, verbose_name='Is this a reply'),
        ),
    ]
