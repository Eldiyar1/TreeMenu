from django.contrib import admin
from .models import Menu, MenuItem

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'parent')