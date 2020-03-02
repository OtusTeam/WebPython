from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return f'{self.title} {self.creation_date}'
