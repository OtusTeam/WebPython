from django.contrib import admin

from .models import Tag, Author, Article


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = 'title', 'creation_date', 'author', 'display_tags'


    def display_tags(self, obj: Article):
        """
        :param obj:
        :return:
        """
        tags = obj.tags.all()
        return ', '.join([t.name for t in tags])

    display_tags.short_description = 'tags'
