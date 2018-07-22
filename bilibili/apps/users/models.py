# _*_ encoding:utf-8 _*_
from datetime import  datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=20,verbose_name=u'昵称')
    birthday = models.DateField(null=True,blank=True,verbose_name=u'生日')
    gender = models.CharField(choices=(('male',u'男'),('female',u'nv ')),max_length=6,
                              default='male',verbose_name=u'性别')
    mobile = models.CharField(max_length=11,null=True,blank=True,verbose_name=u'手机')
    image = models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",max_length=100,
                              verbose_name=u'头像')
    sign = models.CharField(max_length=200,default='',verbose_name=u'签名')

    class Meta:
        verbose_name=u'用户信息'
        verbose_name_plural=verbose_name


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name=u'验证码')
    email = models.EmailField(max_length=50,verbose_name=u'邮箱')
    send_type= models.CharField(choices=(('register',u'注册'),('forget',u'忘记密码'),('update_email',u'修改邮箱')),
                                max_length=15,verbose_name=u'验证码类型')
    send_time = models.DateTimeField(default=datetime.now,verbose_name=u'发送时间')

    class Meta:
        verbose_name=u'邮箱验证码'
        verbose_name_plural=verbose_name