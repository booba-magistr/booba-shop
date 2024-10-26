from django.contrib import admin
from .models import Review

# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    fields = 'user', 'time_create', 'review'
    list_display = 'user', 'time_create', 'review'
    readonly_fields = 'time_create',