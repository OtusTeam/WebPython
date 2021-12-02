from django.contrib.auth import get_user_model
from django.db import models


class Author(models.Model):
    STATUS_JR = 'J'
    STATUS_MD = 'M'
    STATUS_SR = 'S'

    STATUS_CHOICES = [
        (STATUS_JR, 'junior'),
        (STATUS_MD, 'middle'),
        (STATUS_SR, 'senior'),
    ]

    user = models.OneToOneField(get_user_model(),
                                on_delete=models.CASCADE,
                                primary_key=True)

    status = models.CharField(max_length=1,
                              choices=STATUS_CHOICES,
                              default=STATUS_JR)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Author <{self.user}>"


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    title = models.CharField(max_length=150)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Article(title={self.title!r}, author={self.author})"
