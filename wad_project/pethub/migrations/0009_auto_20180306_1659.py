# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-06 16:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pethub', '0008_post_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='user_profile',
        ),
    ]