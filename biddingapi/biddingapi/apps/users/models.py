from django.db import models
from django.contrib.auth.models import AbstractUser
from biddingapi.apps.bid.spider_bidding.config import crux
# Create your models here.
class User(AbstractUser):
    """用户模型类"""

    id = models.AutoField(primary_key=True)     # 如果表里面没有写主键，表里面会自动生成一个自增主键字段，叫做id字段，orm要求每个表里面必须要写一个主键

    key_word = models.TextField(null=True,default=crux)                   # 关键词库
    time_day = models.IntegerField(null=True,default=1)    # 当前时间点前几天的天数
    url_id = models.CharField(max_length=500,null=True,default=['1'])       # 选择网站的id
    sending_time = models.DateTimeField(null=True,blank=True)           # 选择每天发送的时间
    email = models.CharField(max_length=80,blank=True,null=True)         # 邮箱
    state = models.BooleanField(null=True,default=False)                   # 状态
    mobile = models.CharField(max_length=15, null=True,unique=True,blank=True, verbose_name='手机号码')
    avatar = models.ImageField(upload_to='avatar',verbose_name='用户头像',null=True,blank=True,default='avatar/touxiang.png')

    class Meta:
        db_table = 'bid_user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name