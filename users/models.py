from django.contrib.auth.models import AbstractUser
from django.db import models

from mainapp.models import NULLABLE


class User(AbstractUser):
    username = None

    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    telegram = models.CharField(max_length=50, verbose_name='телеграм', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', **NULLABLE)

    email = models.EmailField(unique=True, verbose_name='почта')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


