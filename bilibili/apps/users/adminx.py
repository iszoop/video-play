# _*_ coding:utf-8 _*_
__author__ = 'iszoop'
__date__ = '2018/7/8 14:43'
import xadmin
from xadmin import views
from .models import UserProfile,EmailVerifyRecord

class BaseSetting(object):
    #设置主题
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    #设置页面标题
    site_title = "bilibili后台管理系统"   #网站标题
    site_footer = "bilibili在线网"        #底部标签
    menu_style = "accordion"              #app详情可收起


class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time']     #列表显示
    search_fields = ['code','email','send_type']    #列表搜索
    list_filter = ['code','email','send_type','send_time']      #列表筛选




xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)