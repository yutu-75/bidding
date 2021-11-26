import re

from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework import serializers
from rest_framework_jwt.compat import get_username_field, PasswordField
from django.utils.translation import ugettext as _
from django.contrib.auth import authenticate, get_user_model
from rest_framework_jwt.settings import api_settings
from . import models
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated

from .utils import get_user_obj

User = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class CustomeSerializer(JSONWebTokenSerializer):

    def __init__(self, *args, **kwargs):
        """
        Dynamically add the USERNAME_FIELD to self.fields.
        """
        super(JSONWebTokenSerializer, self).__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields['password'] = PasswordField(write_only=True)



    #
    def validate(self, attrs):
        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password'),

            # 'email': attrs.get('email'),


        }
        # {'username':'root',password:'123'}

        if all(credentials.values()):
            print(credentials)
            user = authenticate(self.context['request'], **credentials)  # self.context['request']当前请求的request对象
            print(user,'ssss')
            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)

                payload = jwt_payload_handler(user)
                print(user)

                return {
                    'token': jwt_encode_handler(payload),
                    'user': user,

                }
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "{username_field}" and "password".')
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)

class  UserSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "key_word", "time_day","url_id","sending_time","email", "state", "avatar","password")


