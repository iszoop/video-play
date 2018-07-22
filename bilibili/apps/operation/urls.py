# _*_ coding:utf-8 _*_
__author__ = 'iszoop'
__date__ = '2018/7/9 16:25'

from django.conf.urls import url
from .views import UserinfoView,MyVideoView,FavouriteUpView,FavouriteVideoView,MyMessageView
from .views import UploadImageView,UpdatePwdView,SendEmailCodeView,UpdateEmailView


urlpatterns = [
    url(r'^info/$',UserinfoView.as_view(), name="user_info"),
    url(r'^my_video/$',MyVideoView.as_view(), name="my_video"),
    url(r'^fav_up/$',FavouriteUpView.as_view(), name="fav_up"),
    url(r'^fav_video/$',FavouriteVideoView.as_view(), name="fav_video"),
    url(r'^my_message/$',MyMessageView.as_view(), name="my_message"),

    url(r'^image/upload/$',UploadImageView.as_view(),name='image_upload'),        #用户头像上传
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name='update_pwd'),            # 个人中心修改密码
    url(r'^sendemail_code/$',SendEmailCodeView.as_view(),name='sendemail_code'), #发送邮箱验证码
    url(r'^update_email/$', UpdateEmailView.as_view(), name='update_email'),     #修改个人邮箱

]