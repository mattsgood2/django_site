# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 11:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_steps'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Steps',
            new_name='Up_next',
        ),
    ]
