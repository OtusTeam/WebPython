from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200, null=False)
    username = models.CharField(max_length=30, null=False, unique=True)

    def __str__(self):
        return self.username


class ToDoItem(models.Model):
    title = models.CharField(max_length=200, null=False)
    done = models.BooleanField(null=False)
    dt_created = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(Author, on_delete=models.PROTECT)
