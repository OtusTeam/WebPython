from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200, default="")
    archived = models.BooleanField(default=False)

    # def get_absolute_url(self):
    #     return

    def __str__(self):
        return self.name
