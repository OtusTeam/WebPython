from django.contrib import admin

from .models import TodoItem, Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'done'
