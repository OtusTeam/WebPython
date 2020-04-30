from django.contrib import admin

from .models import Author, ToDoItem


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'


@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'done'
