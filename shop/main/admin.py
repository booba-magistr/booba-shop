from django.contrib import admin
from .models import Stuff, Contact
from django.utils.safestring import mark_safe


# Register your models here.
@admin.register(Stuff)
class StuffAdmin(admin.ModelAdmin):
    list_display = 'name', 'post_photo', 'slug', 'email', 'phone_number', 'description'
    fields = 'name', 'last_name', 'slug', 'post_photo', 'img', 'email', 'phone_number', 'description'
    prepopulated_fields = {'slug': ('name', 'last_name')}
    readonly_fields = ("post_photo",)
    search_fields = ("name", "description")
    list_editable = ("email", "phone_number")

    @admin.display(description="Опубликовать фото")
    def post_photo(self, stuff: Stuff):
        if stuff.img:
            return mark_safe(f"<img src='{stuff.img.url}' width=100>")
        return "Photo doesn't exist"
    

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'name', 'post_photo','phone_number', 'email', 'address'
    fields = 'name', 'img','post_photo', 'phone_number', 'email', 'address', 'title_img'
    list_editable = ("email", "phone_number")
    readonly_fields = ("post_photo",)

    @admin.display(description="Опубликовать фото")
    def post_photo(self, contact: Contact):
        if contact.img:
            return mark_safe(f"<img src='{contact.img.url}' width=100>")
        return "Photo doesn't exist"
