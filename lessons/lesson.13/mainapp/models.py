from django.db import models

# Катерия - Медведь Тигр
# Животное - Тигр Борис
# Еда

# тигр - мясо
# медведь - мясо
# обезьяна - банан, мясо


# Abstract, Proxy, Table inheritance
class TimeStampMixin(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampMixin):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'


class Food(TimeStampMixin):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Animal(TimeStampMixin):
    name = models.CharField(max_length=64)
    # 1 - 1, 1 - *, * - *
    # 1 категория - много животных
    # cascad, protect, null
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    food = models.ManyToManyField(Food)

    def get_category_name(self):
        return self.category.name


# class WildAnimal(models.Model):
#     animal = models.OneToOneField(Animal)
#
#
# class HomeAnimal(models.Model):
#     animal = models.OneToOneField(Animal)
#     last_owner_name = models.CharField(max_length=32, blank=True, null=True)

# ЯВЛЯЕТСЯ?
class WildAnimal(Animal):
    age = models.PositiveIntegerField(default=0)


class HomeAnimal(Animal):
    last_owner_name = models.CharField(max_length=32, blank=True, null=True)


class LoggingAnimal(Animal):

    class Meta:
        proxy = True

    def get_category_name(self):
        print('LOGGING = True')
        result = super().get_category_name()
        print('GET NAME', result)
        return result


class AnimalCard(TimeStampMixin):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)