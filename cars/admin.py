from django.contrib import admin
from .models import Shop, Cars


@admin.register(Shop)
class shopAdmin(admin.ModelAdmin):
    ...


@admin.register(Cars)
class carsAdmin(admin.ModelAdmin):
    ...
