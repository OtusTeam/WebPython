from django.db import models


class Article(models.Model):

    Types = (
        (1, 'News'),
        (2, 'Announcements'),
    )

    title = models.CharField(max_length=50)
    body = models.TextField()
    type = models.IntegerField(choices=Types)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} {self.title!r}'
