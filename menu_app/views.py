from django.shortcuts import render, get_object_or_404
from .models import Menu, MenuItem

def menu_view(request, menu_name):
    menu = get_object_or_404(Menu, name=menu_name)
    menu_items = MenuItem.objects.filter(menu=menu)
    return render(request, 'menu.html', context={'menu': menu, 'menu_items': menu_items})
