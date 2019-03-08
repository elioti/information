from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(models.Model):
    account = models.CharField("账户", max_length=32)
    name = models.CharField("姓名", max_length=32, default='')
    phone = models.CharField("手机号", max_length=32, default='')
    qq = models.CharField("qq", max_length=32, default='')
    email = models.CharField("邮箱", max_length=32, default='')
    wechat = models.CharField("微信", max_length=32, default='')
    datetime = models.DateTimeField("建立时间", auto_created=True)

    def __str__(self):
        return str(self.account)


class SiteAdmin(AbstractUser):
    """
    网站管理员
    """

    def __str__(self):
        return str(self.username)
