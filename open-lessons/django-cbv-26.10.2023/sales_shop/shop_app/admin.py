from django.contrib import admin

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "id", "name", "description_short"
    list_display_links = "id", "name"

    def description_short(self, obj: Category):
        if len(obj.description) < 50:
            return obj.description

        return f"{obj.description[:50]}..."
