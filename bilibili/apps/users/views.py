from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate,login,logout
from django.http import  HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.hashers import make_password

from .forms import LoginForm,RegisterForm,ForgetForm,ModifyPwdForm
from users.models import UserProfile
from operation.models import UserMessage
from utils.send_email import send_register_email
from .models import EmailVerifyRecord
# Create your views here.
class LoginView(View):
    """
    用户登入
    """
    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username","")
            pass_word = request.POST.get("password","")
            user = authenticate(username=user_name,password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request,'login.html',{'msg':'用户未激活'})
            else:
                return render(request, 'login.html', {'msg': '用户账号或者密码错误'})
        else:
            return render(request,"login.html",{"login_form": login_form})

    def get(self,request):
        return render(request, "login.html", {})


class LogoutView(View):
    """
    用户登出
    """
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))

class RegisterView(View):
    """
    用户注册
    """
    def get(self,request):
        register_form = RegisterForm()
        return render(request, "register.html", {
            "register_form":register_form,
        })

    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name=request.POST.get("email","")
            if UserProfile.objects.filter(email=user_name):
                return render(request,'register.html',{
                    'register_form': register_form,
                    'msg': "用户已经存在"
                })
            pass_word = request.POST.get("password","")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password =make_password(pass_word)
            user_profile.is_active = False
            user_profile.save()

            #写入欢迎注册消息
            user_message = UserMessage()
            user_message.user = user_profile.id
            user_message.message="欢迎注册哔哩哔哩弹幕网！"
            user_message.save()

            send_register_email(user_name, "register")
            return HttpResponse("激活邮件已经发送！")
        else:
            return render(request, "register.html", {'register_form': register_form})


class ActiveUserView(View):
    """
    激活账号
    """
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                get_email = record.email
                user = UserProfile.objects.get(email=get_email)
                user.is_active = True
                user.save()
        else:
            return render(request, "active_fail.html")
        return render(request, "login.html", {})



class ForgetPwdView(View):
    """
    忘记密码
    """
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, "forgetpwd.html", {"forget_form": forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email", "")
            send_register_email(email, "forget")
            return render(request, "send_success.html")
        else:
            return render(request, "forgetpwd.html", {"forget_form": forget_form})


class ResetUserView(View):
    """
    重置密码邮件验证
    """
    def get(self,request,active_code):
        all_recodes = EmailVerifyRecord.objects.filter(code=active_code)
        if all_recodes:
            for recode in all_recodes:
                get_email = recode.email
                return render(request,"password_reset.html",{"email":get_email})
        else:
            return render(request,"active_fail.html")
        return render(request,'login.html',{})


class ModifyPwdView(View):
    """
    重置密码
    """
    def post(self,request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1","")
            pwd2 = request.POST.get("password2","")
            email = request.POST.get("email","")
            if pwd1 != pwd2:
                return render(request,"password_reset.html",{"email":email,"msg":"密码不一致"})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()

            return render (request,"login.html")
        else:
            email = request.POST.get("email","")
            return render(request, "password_reset.html", {"email": email, "modify_form": modify_form})
