# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-01 20:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='occupants_counts',
            new_name='occupants',
        ),
    ]
