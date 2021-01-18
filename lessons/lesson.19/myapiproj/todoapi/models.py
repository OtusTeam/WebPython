from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ToDoItem(models.Model):
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False, null=False)

    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.title} [{'V' if self.done else 'X'}]"
