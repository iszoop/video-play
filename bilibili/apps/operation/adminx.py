# _*_ coding:utf-8 _*_
__author__ = 'iszoop'
__date__ = '2018/7/8 15:06'
import xadmin
from xadmin import views
from .models import VideoComments,UserFavourite,UserMessage

class VideoCommentsAdmin(object):
    list_dispaly = ['user', 'video', 'comments','add_time']
    search_fields = ['user', 'video', 'comments']
    list_filter = ['user', 'video', 'comments','add_time']


class UserFavouriteAdmin(object):
    list_dispaly = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


class UserMessageAdmin(object):
    list_dispaly = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


xadmin.site.register(VideoComments,VideoCommentsAdmin)
xadmin.site.register(UserFavourite,UserFavouriteAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)