import uuid
import datetime

from django.core.cache import cache
from django.contrib.auth.hashers import make_password, check_password

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .models import NewUser
from .serializers import CustomUserSerializer

class CustomUserCreate(APIView):
    # permission_classes = [AllowAny]

    def post(self, request, format='json'):
        print(request.data)
        serializer = CustomUserSerializer(data=request.data)
        # username = request.data.get('username')
        # password = request.data.get('password')
        # email = request.data.get('email')

        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomUserLogin(APIView):
    # permission_classes = [AllowAny]

    def post(self, request, format='json'):
        print(request.data)
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = NewUser.objects.get(username=username)
            print(user)
        except Exception as e:
            return Response({'msg': e}, status=status.HTTP_404_NOT_FOUND)

        print(check_password(password, user.password))
        if not check_password(password, user.password):
            return Response({'msg': 'password error!'}, status=status.HTTP_404_NOT_FOUND)

        token = uuid.uuid4().hex
        print(token, uuid.uuid4())
        # cache.set(token, user.id, timeout=60 * 60)
        data = {
            'msg': 'login success!',
            'token': token,
        }
        return Response(data, status=status.HTTP_200_OK)


class CustomUserChangePWD(APIView):
    # permission_classes = [AllowAny]

    def post(self, request, format='json'):
        print(request.data)
        username = request.data.get('username')
        password = request.data.get('password')
        newpassword = request.data.get('newpassword')
        try:
            user = NewUser.objects.get(username=username)
            print(user)
            print(user.password)
        except Exception as e:
            return Response({'msg': e}, status=status.HTTP_404_NOT_FOUND)
        if not check_password(password, user.password):
            return Response({'msg': 'old password error!'}, status=status.HTTP_404_NOT_FOUND)

        user.set_password(newpassword)
        user.save()
        data = {
            'msg': '密码修改成功!',
        }
        return Response(data, status=status.HTTP_200_OK)


class CustomUserInfo(APIView):
    # permission_classes = [AllowAny]

    def post(self, request, format='json'):
        username = request.data.get('username')
        try:
            user_data = NewUser.objects.filter(username=username).values_list('username', 'email', 'start_date')
        except:
            print('读取数据库失败')
            return Response({'msg': '获取数据失败'})
        print(user_data)
        data = {}
        data['username'] = user_data[0][0]
        data['email'] = user_data[0][1]
        data['start_date'] = user_data[0][2].strftime('%Y-%m-%d')
        return Response(data, status=status.HTTP_200_OK)


