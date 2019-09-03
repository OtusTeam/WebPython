from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name