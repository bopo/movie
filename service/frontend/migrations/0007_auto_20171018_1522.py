# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 15:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_auto_20171018_1518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='pub_date',
            new_name='created',
        ),
    ]
