# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-02 17:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbor', '0006_auto_20191102_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
