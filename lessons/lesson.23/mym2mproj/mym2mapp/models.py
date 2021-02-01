from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Author(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(UserModel, on_delete=models.PROTECT)

    @property
    def full_name(self):
        if not (self.user.first_name or self.user.last_name):
            return self.user.username
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return self.full_name


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)
