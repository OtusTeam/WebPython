from django.contrib import admin
from django.db.models import F

from .models import Tag, Author, Article


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = "id", "name"
    list_display_links = "id", "name"


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(user_username=F("user__username"))

    def username(self, obj: Author):
        return obj.user_username

    list_display = "id", "date_joined", "username"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # qs = qs.select_related("author")
        qs = qs.prefetch_related("tags")
        return qs.annotate(author_username=F("author__user__username"))

    def author_username(self, obj: Article):
        return obj.author_username

    def body_short(self, obj: Article):
        if len(obj.body) < 50:
            return obj.body
        return obj.body[:50] + "..."

    def display_tags(self, obj: Article):
        tags = obj.tags.all()
        return ", ".join((tag.name for tag in tags))

    list_display = "id", "title", "body_short", "author_username", "display_tags"
