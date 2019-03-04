from django.db import models

# Create your models here.


class User(models.Model):
    account = models.CharField("账户", max_length=32)
    name = models.CharField("姓名", max_length=32)
    phone = models.CharField("手机号", max_length=32)
    qq = models.CharField("qq", max_length=32)
    email = models.CharField("邮箱", max_length=32)
    wechat = models.CharField("微信", max_length=32)
