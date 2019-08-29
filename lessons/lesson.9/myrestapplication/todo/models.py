from django.db import models


class ToDoItem(models.Model):

    text = models.CharField(max_length=250)
    done = models.BooleanField(default=False)
    comment = models.CharField(max_length=250, default='')

    def __str__(self):
        return f'To Do: {self.text!r} ({"" if self.done else "not "}done)'
