# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 07:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20160721_1519'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created', '-rating']},
        ),
    ]
