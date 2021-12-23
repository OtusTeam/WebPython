from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model


class OtusUser(AbstractUser):
    email = models.EmailField(unique=True)
    # avatar = models.ImageField(upload_to='avatars', blank=True)
    # is_male = models.BooleanField(default=True)


# class OtusUser(Model):
#     user = models.OneToOneField(User,
#                                 primary_key=True,
#                                 on_delete=models.CASCADE)
#     # avatar = models.ImageField(upload_to='avatars', blank=True)
#     # is_male = models.BooleanField(default=True)
