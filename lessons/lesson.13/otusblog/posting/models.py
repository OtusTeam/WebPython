from django.contrib.auth import get_user_model
from django.db import models


class Author(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.PROTECT, null=False)

    status = models.CharField(max_length=200, null=False, default="", blank=True)
    bio = models.TextField(null=False, default="", blank=True)

    def __str__(self):
        return f"Author <{self.user}>"


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    title = models.CharField(max_length=150, null=False, default="", blank=False)
    text = models.TextField(null=False, default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Article(title={self.title!r}, author={self.author})"
