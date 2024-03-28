from django.contrib import admin
from .models import Shop, Cars


@admin.register(Shop)
class shopAdmin(admin.ModelAdmin):
    ...


@admin.register(Cars)
class carsAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'is_published', 'date',]
    list_filter = ['id', 'author', 'title', 'is_published', 'date',]
    list_editable = ['is_published',]
    search_fields = 'id', 'description', 'title'
    prepopulated_fields = {
        "slug": ('title',)
    }
    autocomplete_fields = ['tags']