from django.contrib import admin

from .models import Author, Article


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = "id", "user", "status", "bio"


# admin.site.register(Author, AuthorAdmin)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # list_display = "id", "author", "title", "text", "created_at", "published_at", "edited_at"
    list_display = "id", "author", "title", "text_short", "published_at", "created_at", "edited_at"

    def text_short(self, obj: Article):
        if len(obj.text) < 40:
            return obj.text
        return f"{obj.text[:36]}..."
