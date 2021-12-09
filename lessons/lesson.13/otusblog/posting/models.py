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


class VipAuthor(Author):
    super_degree = models.PositiveSmallIntegerField(default=1)


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    title = models.CharField(max_length=150)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Article(title={self.title!r}, author={self.author})"


class DescArticle(Article):
    def description(self):
        return self.text[:20]

    class Meta:
        proxy = True


class ArticleAbstract(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    title = models.CharField(max_length=150)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)
    edited_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ShortTitleArticle(ArticleAbstract):
    title = models.CharField(max_length=64)


class TemporaryArticle(ArticleAbstract):
    created_at = None
    published_at = None
    edited_at = None
