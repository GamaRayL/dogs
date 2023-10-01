from django.contrib.auth.models import AbstractUser
from django.db import models

from mainapp.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []