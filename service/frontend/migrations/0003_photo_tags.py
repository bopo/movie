# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20170922_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='tags',
            field=models.ManyToManyField(to='frontend.Tags'),
        ),
    ]
