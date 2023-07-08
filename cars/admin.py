from django.contrib import admin
from .models import Shop


class carsAdmin(admin.ModelAdmin): 
    ...


admin.site.register(Shop, carsAdmin)