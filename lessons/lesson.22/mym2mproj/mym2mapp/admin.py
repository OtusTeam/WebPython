from django.contrib import admin

from .models import Tag, Author, Article


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = "id", "first_name", "last_name", "full_name"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = "id", "name"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        if request.method != 'GET':
            return Article.objects.filter()
        return Article.objects.filter().prefetch_related("tags")

    def body_short(self, obj: Article):
        if len(obj.body) > 50:
            return f"{obj.body[:50]}..."
        return obj.body

    def display_tags(self, obj: Article):
        tags = obj.tags.all()
        return ", ".join((t.name for t in tags))

    list_display = "id", "title", "body_short", "author", "display_tags"
