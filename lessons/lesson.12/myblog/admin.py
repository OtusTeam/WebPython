from django.contrib import admin

from .models import Author, Article


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = "id", "first_name", "last_name", "full_name"
    list_display_links = "id", "full_name"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    def text_short(self, obj: Article):
        if len(obj.text) > 42:
            return f"{obj.text[:42]}..."
        return obj.text

    list_display = "id", "title", "text_short", "time_to_read", "ts_created", "ts_last_changed", "author"
    list_display_links = "id", "title", "text_short"
