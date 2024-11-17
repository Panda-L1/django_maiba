# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=20,null=True)  # 昵称
    age = models.IntegerField(null=True)  # 年龄

    def __str__(self):
        return self.username
    class Meta:
        db_table = 'users'
