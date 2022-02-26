from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class LoginLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User ID")
    date_login = models.DateTimeField(auto_now_add=True, verbose_name="Last Logged In")
