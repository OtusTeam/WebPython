from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Article(models.Model):
    TTR_L_1 = 1
    TTR_1_5 = 2
    TTR_5_15 = 3
    TTR_15_30 = 4
    TTR_G_30 = 5

    TIME_TO_READ = (
        (TTR_L_1, '< 1 min'),
        (TTR_1_5, '1-5 min'),
        (TTR_5_15, '5-15 min'),
        (TTR_15_30, '15-30 min'),
        (TTR_G_30, '> 30 min'),
    )

    title = models.CharField(max_length=254)
    text = models.TextField()
    time_to_read = models.IntegerField(choices=TIME_TO_READ)
    ts_last_changed = models.DateTimeField(auto_now=True)
    ts_created = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
