from django.contrib import admin
from .models import Animal, Category, Food, WildAnimal, HomeAnimal

admin.site.register(Category)
admin.site.register(Food)

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

admin.site.register(Animal, AnimalAdmin)

admin.site.register(WildAnimal, AnimalAdmin)


class HomeAnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'last_owner_name')

admin.site.register(HomeAnimal, HomeAnimalAdmin)
