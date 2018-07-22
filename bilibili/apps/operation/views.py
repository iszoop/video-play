from django.shortcuts import render
from django.views.generic.base import View
from django.http import  HttpResponse
from django.contrib.auth.hashers import make_password

from videos.models import Video
from .models import UserFavourite,UserMessage
from .forms import UploadImageForm,UserInfoForm
from users.forms import ModifyPwdForm
from users.models import UserProfile,EmailVerifyRecord
from utils.send_email import send_register_email
from utils.mixin_utils import LoginRequiredMixin

import json
# Create your views here.


class UserinfoView(LoginRequiredMixin,View):
    """
    用户个人信息
    """
    def get(self,request):
        return render(request,"usercenter-info.html",{})

    def post(self,request):
        user_info_form = UserInfoForm(request.POST,instance=request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse(json.dumps(user_info_form.errors), content_type='application/json')


class SendEmailCodeView(LoginRequiredMixin,View):
    """
    发送邮箱验证
    """
    def get(self,request):
        email = request.GET.get("email","")
        if UserProfile.objects.filter(email=email):
            return HttpResponse('{"email":"邮箱已经被注册！"}',content_type='application/json')
        send_register_email(email,"update_email")
        return HttpResponse('{"status":"success"}', content_type='application/json')


class UpdateEmailView(LoginRequiredMixin,View):
    """
    修改个人邮箱
    """
    def post(self,request):
        email = request.POST.get("email","")
        code = request.POST.get("code","")

        exist_code = EmailVerifyRecord.objects.filter(email=email,code=code,send_type="update_email")
        if exist_code:
            user = request.user
            user.email = email
            user.username = email
            user.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"email":"验证码出错！"}', content_type='application/json')



class MyVideoView(LoginRequiredMixin,View):
    def get(self,request):
        user_video = Video.objects.filter(contributor=request.user)
        return render(request,"usercenter-myvideo.html",{
            'user_video':user_video,
        })


class FavouriteUpView(LoginRequiredMixin,View):
    def get(self,request):
        fav_up = UserFavourite.objects.filter(user=request.user,fav_type=2)
        return render(request, "usercenter-fav-up.html", {
            'fav_up': fav_up,
        })


class FavouriteVideoView(LoginRequiredMixin,View):
    def get(self,request):
        fav_video = UserFavourite.objects.filter(user=request.user,fav_type=1)
        return render(request, "usercenter-fav-video.html", {
            'fav_video': fav_video,
        })


class MyMessageView(LoginRequiredMixin,View):
    def get(self,request):
        all_message = UserMessage.objects.filter(user=request.user.id)
        return render(request, "usercenter-message.html", {
            'all_message': all_message,
        })


class UploadImageView(LoginRequiredMixin,View):
    """
    用户修改头像
    """
    def post(self,request):
        image_form = UploadImageForm(request.POST,request.FILES,instance=request.user)
        if image_form.is_valid():
            image_form.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail"}', content_type='application/json')


class UpdatePwdView(LoginRequiredMixin,View):
    def post(self, request):
        """个人中心修改用户密码"""
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            if pwd1 != pwd2:
                return HttpResponse('{"status":"fail","msg":"密码不一致"}', content_type='application/json')
            user=request.user
            user.password=make_password(pwd2)
            user.save()

            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse(json.dumps(modify_form.errors), content_type='application/json')