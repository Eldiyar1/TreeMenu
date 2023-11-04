from django import template

from menu_app.models import Menu, MenuItem

register = template.Library()

@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu = Menu.objects.get(name=menu_name)
    menu_items = MenuItem.objects.filter(menu=menu).select_related('parent')
    current_url = context['request'].path
    return {'menu_items': menu_items, 'current_url': current_url}
