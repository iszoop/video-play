# _*_ coding:utf-8 _*_
__author__ = 'iszoop'
__date__ = '2018/7/9 21:00'

from django import forms

from captcha.fields import CaptchaField

from .models import UserProfile

class UploadImageForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['image']


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name','birthday','gender','sign','mobile']