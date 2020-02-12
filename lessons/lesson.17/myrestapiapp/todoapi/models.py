from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    title = models.CharField(max_length=50)
    done = models.BooleanField()
    author = models.ForeignKey(Author, models.PROTECT)

    def __str__(self):
        return f'{self.title} [{"V" if self.done else "X"}]'
