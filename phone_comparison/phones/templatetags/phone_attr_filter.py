from django import template

register = template.Library()

@register.filter
def check_attr(value):
    if value:
        return 'Есть'
    return '-'
