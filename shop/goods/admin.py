from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "post_photo",
        "description",
        "price",
        "discount",
        "count",
        "cat",
    )
    prepopulated_fields = {"slug": ("name",)}
    fields = (
        "name",
        "slug",
        "post_photo",
        "img",
        "description",
        "price",
        "discount",
        "count",
        "cat",
    )
    readonly_fields = ("post_photo",)
    list_per_page = 8
    list_editable = ("price", "count", "discount")
    search_fields = ("name", "description")

    @admin.display(description="Опубликовать фото")
    def post_photo(self, product: Product):
        if product.img:
            return mark_safe(f"<img src='{product.img.url}' width=100>")
        return "Photo doesn't exist"
