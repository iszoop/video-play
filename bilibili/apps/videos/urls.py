# _*_ coding:utf-8 _*_
__author__ = 'iszoop'
__date__ = '2018/7/10 13:44'

from django.conf.urls import url,include

from .views import VideoPlayView

urlpatterns = [
    url(r'^play/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name="video_paly"),          #视频播放页面
]