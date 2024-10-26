from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
class OrderItemTabularAdmin(admin.TabularInline):
    model = OrderItem
    fields = "product", "name", "price", "quantity"
    search_fields = (
        "product",
        "name",
    )
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = "order", "product", "name", "price", "quantity"
    search_fields = (
        "order",
        "product",
        "name",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "phone_number",
        "time_create",
        "status"
    )
    list_editable = ("status",)
    search_fields = ("user",)
    inlines = (OrderItemTabularAdmin,)
    readonly_fields = ("time_create",)