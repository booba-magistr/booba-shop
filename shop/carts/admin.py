from django.contrib import admin
from .models import Carts

# Register your models here.
class UserCartAdmin(admin.TabularInline):
    model = Carts
    fields = "product", "quantity", "created_timestamp"
    search_fields = ("product", )
    readonly_fields = ("created_timestamp", )
    extra = 1


@admin.register(Carts)
class CartsAdmin(admin.ModelAdmin):
    list_display = ("user", "session_key", "created_timestamp", "product", "quantity")
    search_fields = ("user",)

