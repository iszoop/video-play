# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-08 05:10
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('image', models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图')),
                ('url', models.URLField(max_length=100, verbose_name='访问地址')),
                ('index', models.IntegerField(default=100, verbose_name='访问地址')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='视频名')),
                ('desc', models.CharField(max_length=400, verbose_name='描述')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('image', models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='投稿时间')),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='UP主')),
            ],
            options={
                'verbose_name': '视频信息',
                'verbose_name_plural': '视频信息',
            },
        ),
        migrations.CreateModel(
            name='VideoType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10, verbose_name='视频类型')),
                ('tag', models.CharField(blank=True, max_length=15, null=True, verbose_name='视频标签')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '视频分类',
                'verbose_name_plural': '视频分类',
            },
        ),
        migrations.AddField(
            model_name='video',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.VideoType', verbose_name='视频类型'),
        ),
    ]
