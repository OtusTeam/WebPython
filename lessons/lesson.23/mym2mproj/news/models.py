from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


class Author(models.Model):
    dt_joined = models.DateTimeField(auto_now_add=True)
    nickname = models.CharField(max_length=30)

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return str(self)


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, related_name="articles")
