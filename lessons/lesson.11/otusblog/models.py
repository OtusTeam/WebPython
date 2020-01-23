from django.db import models
from django.db.models import ForeignKey


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.id} {self.full_name}'


class Article(models.Model):
    CATEGORIES = (
        (1, 'News'),
        (2, 'Announcements'),
    )
    title = models.CharField(max_length=40)
    body = models.TextField()
    category = models.IntegerField(choices=CATEGORIES)

    author = ForeignKey(Author, models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.title}'
