# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_auto_20171018_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weblink',
            name='url',
        ),
        migrations.AddField(
            model_name='weblink',
            name='link',
            field=models.URLField(default=1, max_length=100, verbose_name='网站链接'),
            preserve_default=False,
        ),
    ]