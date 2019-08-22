from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    def short_body(self, obj: Article):
        return f'{obj.body[:30]}...'

    list_display = ('id', 'title', 'short_body', 'pub_date')
