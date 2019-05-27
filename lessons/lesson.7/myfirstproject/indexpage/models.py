from django.db import models


class Article(models.Model):

    ARTICLE_TYPES = (
        (1, 'Type 1'),
        (2, 'Type 2'),
    )

    title = models.CharField(max_length=50)
    body = models.TextField()
    type = models.IntegerField(choices=ARTICLE_TYPES)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} from {self.pub_date}'
