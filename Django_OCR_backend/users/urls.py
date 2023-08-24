from django.urls import path

from .views import CustomUserCreate, CustomUserLogin, CustomUserChangePWD, CustomUserInfo

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name='create_user'),
    path('login/', CustomUserLogin.as_view(), name='login_user'),
    path('changePWD/', CustomUserChangePWD.as_view(), name='changePWD'),
    path('info/', CustomUserInfo.as_view(), name='info'),
]
