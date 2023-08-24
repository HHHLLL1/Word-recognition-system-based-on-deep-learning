from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    username = models.CharField(max_length=150, null=False)
    file = models.FileField(upload_to='post_files', default='file', null=False)
    filetype = models.CharField(max_length=150)
    text = models.CharField(max_length=10000)
    uploaded = models.DateTimeField(default=timezone.now)
    # slug = models.SlugField(max_length=250, unique_for_date='uploaded')


    def __str__(self):
        return self.username
