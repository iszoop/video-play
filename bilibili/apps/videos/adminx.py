# _*_ coding:utf-8 _*_
__author__ = 'iszoop'
__date__ = '2018/7/8 14:59'

import xadmin
from xadmin import views
from .models import VideoType,Video,Banner

class VideoTypeAdmin(object):
    list_dispaly = ['type','add_time']
    search_fields = ['type']
    list_filter = ['type','add_time']


class VideoAdmin(object):
    list_dispaly = ['contributor', 'name', 'desc','type','fav_nums','click_nums','tag','add_time']
    search_fields = ['contributor', 'name', 'desc','type','fav_nums','tag','click_nums']
    list_filter = ['contributor', 'name', 'desc','type','fav_nums','click_nums','tag','add_time']


class BannerAdmin(object):
    list_dispaly = ['title', 'url', 'index', 'add_time']
    search_fields = ['title', 'url', 'index']
    list_filter = ['title', 'url', 'index', 'add_time']


xadmin.site.register(VideoType,VideoTypeAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(Banner,BannerAdmin)


