from django.contrib.auth.models import AbstractUser
from django.db import models


class OtusUser(AbstractUser):
    email = models.EmailField(unique=True)
    # avatar = models.ImageField(upload_to='avatars', blank=True)
    # is_male = models.BooleanField(default=True)
