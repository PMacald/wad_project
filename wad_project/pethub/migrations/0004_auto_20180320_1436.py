# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-20 14:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pethub', '0003_auto_20180320_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='pethub.Post'),
        ),
    ]
