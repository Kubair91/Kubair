# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-09 17:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='C',
            new_name='C_Program',
        ),
        migrations.RenameModel(
            old_name='Java',
            new_name='Java_Program',
        ),
        migrations.RenameModel(
            old_name='Python',
            new_name='Python_Program',
        ),
    ]
