from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Article(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()

    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, related_name="articles")

    def __str__(self):
        return self.title
