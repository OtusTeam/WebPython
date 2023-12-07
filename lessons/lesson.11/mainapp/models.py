from django.db import models

# Катерия - Медведь Тигр
# Животное - Тигр Борис
# Еда

# тигр - мясо
# медведь - мясо
# обезьяна - банан, мясо


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'


class Food(models.Model):
    name = models.CharField(max_length=64)


class Animal(models.Model):
    name = models.CharField(max_length=64)
    # 1 - 1, 1 - *, * - *
    # 1 категория - много животных
    # cascad, protect, null
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    food = models.ManyToManyField(Food)
