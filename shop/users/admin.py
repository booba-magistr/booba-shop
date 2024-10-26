from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from carts.admin import UserCartAdmin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email")
    inlines = (UserCartAdmin, )