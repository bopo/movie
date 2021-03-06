# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_photo_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Short descriptive name for this category.', max_length=200, verbose_name='分类标题')),
            ],
            options={
                'verbose_name': '地区',
                'verbose_name_plural': '地区管理',
            },
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Short descriptive name for this category.', max_length=200, verbose_name='分类标题')),
            ],
            options={
                'verbose_name': '类别',
                'verbose_name_plural': '类别管理',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='网站名称')),
                ('icon', models.URLField(max_length=100, verbose_name='网站图标')),
                ('url', models.URLField(max_length=100, verbose_name='网站URL')),
            ],
            options={
                'verbose_name': '评论管理',
                'verbose_name_plural': '评论管理',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Short descriptive name for this category.', max_length=200, verbose_name='导演名称')),
            ],
            options={
                'verbose_name': '导演',
                'verbose_name_plural': '导演管理',
            },
        ),
        migrations.CreateModel(
            name='Live',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Short descriptive name for this tag.', max_length=200)),
                ('slug', models.SlugField(help_text='Short descriptive unique name for use in urls.', max_length=255, unique=True)),
            ],
            options={
                'verbose_name': '直播',
                'verbose_name_plural': '直播管理',
            },
        ),
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Short descriptive name for this category.', max_length=200, verbose_name='分类标题')),
            ],
            options={
                'verbose_name': '演员',
                'verbose_name_plural': '演员管理',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='相册标题')),
                ('slug', models.CharField(max_length=64, verbose_name='相册标示')),
                ('cover', models.ImageField(upload_to='cover/', verbose_name='封面相册')),
                ('photolist', models.TextField(default='', verbose_name='图片列表')),
                ('views', models.IntegerField(default=0, verbose_name='浏览数')),
                ('likes', models.IntegerField(default=0, verbose_name='喜欢数')),
                ('count', models.IntegerField(default=0, verbose_name='相册数')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='发布时间')),
                ('ordering', models.IntegerField(default=9999, verbose_name='排序')),
                ('recommend', models.BooleanField(default=0, verbose_name='推荐')),
                ('status', models.BooleanField(default=False, verbose_name='发布状态')),
            ],
            options={
                'verbose_name': '视频',
                'verbose_name_plural': '视频管理',
            },
        ),
        migrations.RemoveField(
            model_name='photo',
            name='category',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='tags',
        ),
        migrations.AlterModelOptions(
            name='weblink',
            options={'verbose_name': '友链', 'verbose_name_plural': '友链管理'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(help_text='Short descriptive unique name for use in urls.', max_length=255, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='category',
            name='subtitle',
            field=models.CharField(blank=True, default='', help_text='Some titles may be the same and cause confusion in admin UI. A subtitle makes a distinction.', max_length=200, null=True, verbose_name='副标题'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(help_text='Short descriptive name for this category.', max_length=200, verbose_name='分类标题'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='slug',
            field=models.SlugField(help_text='Short descriptive unique name for use in urls.', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='tags',
            name='title',
            field=models.CharField(help_text='Short descriptive name for this tag.', max_length=200),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.AddField(
            model_name='video',
            name='category',
            field=models.ManyToManyField(to='frontend.Category'),
        ),
        migrations.AddField(
            model_name='video',
            name='channel',
            field=models.ManyToManyField(to='frontend.Channel'),
        ),
        migrations.AddField(
            model_name='video',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Comment'),
        ),
        migrations.AddField(
            model_name='video',
            name='tags',
            field=models.ManyToManyField(to='frontend.Tags'),
        ),
        migrations.AddField(
            model_name='category',
            name='channel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontend.Channel', verbose_name='隶属于'),
        ),
    ]
