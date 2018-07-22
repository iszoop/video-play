# _*_ encoding:utf-8 _*_
from datetime import  datetime
from django.db import models

from users.models import UserProfile
# Create your models here.

class VideoType(models.Model):
    type = models.CharField(max_length=10,verbose_name=u'视频类型')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type


class Video(models.Model):
    contributor = models.ForeignKey(UserProfile,verbose_name=u'UP主')
    name = models.CharField(max_length=50,verbose_name=u'视频名')
    desc = models.CharField(max_length=400,verbose_name=u'描述')
    type = models.ForeignKey(VideoType,verbose_name=u'视频类型')
    fav_nums = models.IntegerField(default=0,verbose_name=u'收藏人数')
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u'封面', max_length=100)
    url = models.CharField(max_length=200, default='', verbose_name=u'访问地址')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    tag = models.CharField(max_length=15, null=True, blank=True, verbose_name=u'视频标签')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'投稿时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name=u'标题')
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u'轮播图', max_length=100)
    url = models.URLField(max_length=100, verbose_name=u'访问地址')
    index = models.IntegerField(default=100,verbose_name=u'访问地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name