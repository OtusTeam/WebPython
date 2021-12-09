from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from myauth.models import OtusUser


@admin.register(OtusUser)
class OtusUserAdmin(UserAdmin):
    list_display = "id", "username", "first_name", "last_name"
