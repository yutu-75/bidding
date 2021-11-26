from urllib.parse import urlencode
import json, urllib
from urllib.request import urlopen
from . import models

from django.conf import settings

from django.db.models import Q
# from biddingapi.settings import contains
from users import models
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend




def get_user_by_account(account):
    """
    根据帐号获取user对象
    :param account: 账号，可以是用户名，也可以是手机号
    :return: User对象 或者 None
    """
    try:


        user = models.User.objects.filter(Q(username=account)|Q(email=account)).first()
        print(user,'user')
    except models.User.DoesNotExist:
        return None
    else:
        return user
class UsernameMobileAuthBackend(ModelBackend):
    """
    自定义用户名或手机号认证
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_user_by_account(username)
        #if user is not None and user.check_password(password) :

        if( user is not None and user.check_password(password)) or self.check_password1(user,password) :
            #user.is_authenticated是看他有没有权限的，这里可以不加上它
            print(user,'ssssss')
            return user
    def check_password1(self,u,p):


        return models.User.objects.filter(username=u,password=p).exists()


def jwt_response_payload_handler(token, user=None, request=None):

    return {
        'token': token,
        'username': user.username,
        'avatar': str(user.avatar),
        # 'id':user.id,
        # 'credit':user.credit,
        # 'credit_to_money':contains.CREDIT_MONEY,
    }



def get_user_obj(accout):  # 666
    try:
        print('ww')
        user_obj = models.User.objects.get(Q(username=accout) | Q(email=accout))
    except:
        return None
    return user_obj







