from django.db import models
from django.contrib.auth.models import AbstractUser

class Collect(models.Model):
    # 需要采集的项目信息
    id = models.AutoField(primary_key=True)     # 如果表里面没有写主键，表里面会自动生成一个自增主键字段，叫做id字段，orm要求每个表里面必须要写一个主键
    web_url = models.CharField(max_length=200)  # 采集网站url
    web_name = models.CharField(max_length=200)  # 采集网站url的名字
    state = models.BooleanField()               # 采集状态
    get_date = models.DateTimeField()               # 录入日期
    crux_word = models.CharField(max_length=500)  # 采集数据的关键字
    # price = models.DecimalField(max_digits=8, decimal_places=2)  # max_digits最大位数，decimal_places小数部分占多少位
    # publish = models.CharField(max_length=32)


class Bidding(models.Model):
    id = models.AutoField(primary_key=True)     # 如果表里面没有写主键，表里面会自动生成一个自增主键字段，叫做id字段，orm要求每个表里面必须要写一个主键
    collect_time = models.DateTimeField()               # 采集日期
    b_title = models.CharField(max_length=500)                  # 和varchar(32)是一样的，32个字符
    b_url = models.CharField(max_length=500)  # 和varchar(32)是一样的，32个字符
    b_release = models.DateTimeField()               # 发标日期
    b_money = models.CharField(max_length=500)
    customer_name = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=50)
    b_time = models.DateTimeField()               # 获取招标文件时间
    notice_type = models.CharField(max_length=50)
    collect = models.ForeignKey(to='Collect',to_field='id', on_delete=models.DO_NOTHING )

# class User(models.Model):



# class User(AbstractUser):
#     """用户模型类"""
#
#     id = models.AutoField(primary_key=True)     # 如果表里面没有写主键，表里面会自动生成一个自增主键字段，叫做id字段，orm要求每个表里面必须要写一个主键
#
#     key_word = models.TextField(null=True)                   # 关键词库
#     time_day = models.IntegerField(null=True)    # 当前时间点前几天的天数
#     url_id = models.CharField(max_length=500,null=True)       # 选择网站的id
#     sending_time = models.DateTimeField(null=True)           # 选择每天发送的时间
#     email = models.CharField(max_length=80,null=True)         # 邮箱
#     state = models.BooleanField(null=True)                   # 状态
#     mobile = models.CharField(max_length=15, unique=True, verbose_name='手机号码')
#     avatar = models.ImageField(upload_to='avatar',verbose_name='用户头像',null=True,blank=True)
#
#     class Meta:
#         db_table = 'bid_user'
#         verbose_name = '用户信息'
#         verbose_name_plural = verbose_name