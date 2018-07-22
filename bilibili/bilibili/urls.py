"""bilibili URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.views.generic import TemplateView
from django.conf.urls import url,include
from users.views import LoginView,LogoutView,ForgetPwdView,RegisterView,ActiveUserView,ResetUserView,ModifyPwdView
import xadmin
from django.views.static import serve

from bilibili.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html"),name="index"),
    url(r'^login/$',LoginView.as_view(),name="login"),                                   #登录页面
    url(r'^logout/$', LogoutView.as_view(), name="logout"),                              #用户登出
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),                       #忘记密码
    url(r'^register/$', RegisterView.as_view(), name="register"),                        #注册账号
    url(r'^active/(?P<active_code>.*)/$',ActiveUserView.as_view(),name="user_active"),   #激活账号
    url(r'^reset/(?P<active_code>.*)/$',ResetUserView.as_view(),name="reset_pwd"),       #重置密码邮箱验证
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),                  #重置密码

    url(r'^captcha/',include('captcha.urls')),                                          #验证码配置

    url(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),                    #配置上传文件的访问处理函数

    url(r'^users/', include('operation.urls', namespace="operation")),                      #用户操作相关配置
    url(r'^videos/', include('videos.urls', namespace="video")),                              #视频相关配置




]
