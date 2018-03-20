# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-20 10:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pethub', '0002_post_liked_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='liked_users',
            field=models.ManyToManyField(default=None, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
