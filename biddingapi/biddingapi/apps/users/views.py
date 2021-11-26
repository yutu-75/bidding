from django.shortcuts import render
from .serializers import CustomeSerializer,UserSelectSerializer
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework.views import APIView
from rest_framework_jwt.utils import jwt_decode_handler
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import User
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CustomLoginView(ObtainJSONWebToken):
    serializer_class = CustomeSerializer

class AvatarView(APIView):
    permission_classes = [IsAuthenticated, ]
    def post(self,request):
        token = request.headers['Authorization']
        print(token)
        try:
            if token:
                token = token.split(' ')[1]

            # 顶一个空数组来接收token解析后的值

            toke_user = jwt_decode_handler(token)
        except Exception as e:
            return Response({'error': f"token值有误！{e}"})
        # 获得user_id
        user_id = toke_user["user_id"]
        file_obj = request.FILES.get('file')
        obj = User.objects.get(pk=user_id)
        obj.avatar = file_obj
        obj.save()
        img_name = obj.avatar

        data = {
            "img_name": str(img_name),
            "code": 200,
            "message": "请求成功"
        }

        return Response(data)

class SettingsView(APIView):
    # User = get_user_model()
    permission_classes = [IsAuthenticated, ]
    def get(self, request):

        # 获取请求参数token的值
        token = request.headers['Authorization']
        # 获得user_id
        user_id = self.get_token(token)
        if not user_id:
            return Response({'error': "token值有误！"})

        user_info = User.objects.get(pk=user_id)
        serializer = UserSelectSerializer(user_info)
        data = {

            "data": serializer.data,
            "code": 200,
            "message": "请求成功"
        }
        print(data)



        return Response(data)

    def post(self, request):
        token = request.headers['Authorization']
        s_data = request.data
        update_dict = {i: s_data[i] for i in s_data if s_data[i] or s_data[i] is False}

        user_id = self.get_token(token)
        if not user_id:
            return Response({'error': "token值有误！"})
        try:
            u_boj = User.objects.filter(pk=user_id).update(
                **update_dict
            )
            return Response('ok!')
        except Exception as e:
            return Response('数据参数或格式有误！',status=400)

    @staticmethod
    def get_token(token):
        # 获取请求参数token的值

        try:
            if token:
                token = token.split(' ')[1]
            toke_user = jwt_decode_handler(token)
        except Exception as e:
            return None
        # 获得user_id
        user_id = toke_user["user_id"]
        return user_id


