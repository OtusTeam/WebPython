from django.contrib import admin

from .models import Author, Article


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'date_joined', 'full_name'
    list_display_links = 'id', 'full_name',


# admin.site.register(Author, AuthorAdmin)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    def body_short(self, obj: Article):
        if len(obj.body) <= 30:
            return obj.body
        return f'{obj.body[:30]}...'

    list_display = 'id', 'title', 'body_short', 'author'
    list_display_links = 'id', 'title', 'author'