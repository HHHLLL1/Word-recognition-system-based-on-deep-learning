from django.conf import settings
from rest_framework import serializers

from .models import Post

class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model = Post
        fields = '__all__'

# class UserRegistrationSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(required=True)
#     username = serializers.CharField(required=True)
#     password = serializers.CharField(min_length=8, write_only=True)
#
#     class Meta:
#         model = settings.AUTH_USER_MODEL
#         fields = ('email', 'username', 'first_name')
#         extra_kwargs = {'password': {'write_only': True}}
