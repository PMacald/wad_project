# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-02 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pethub', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='user_images'),
        ),
    ]