from django.contrib import admin

from .models import Tag, Author, Article


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = "id", "name"
    list_display_links = "id", "name"


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = "id", "nickname", "dt_joined"
    list_display_links = "id", "nickname"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = "id", "title", "author", "body_short", "created_at", "author_id", "display_tags"
    list_display_links = "id", "title"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related("tags")

    def body_short(self, obj: Article):
        if len(obj.body) > 30:
            return f"{obj.body[:28]}..."
        return obj.body

    def display_tags(self, obj: Article):
        tags = obj.tags.all()
        return ", ".join((tag.name for tag in tags))
