from django.contrib import admin
from django.db.models import Q

from .models import Author, Article


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = 'id', 'full_name', 'email'
    list_display_links = 'full_name',


# admin.site.register(Author, AuthorAdmin)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'text_short', 'status', 'last_changed', 'created'
    list_display_links = 'title', 'text_short'
    ordering = '-last_changed',
    list_filter = ('status', )

    def text_short(self, obj: Article):
        if len(obj.text) < 40:
            return obj.text
        return f'{obj.text[:40]}...'

    def get_queryset(self, request):
        # return Article.objects.all().order_by('title')
        if request.user.is_superuser:
            return Article.objects.all()
        return Article.objects.filter(~Q(status=Article.DRAFT))
