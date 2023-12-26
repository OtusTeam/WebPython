from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


class MyUser(AbstractUser):
    email = models.EmailField(unique=True)
