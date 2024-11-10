# core/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(int(key), 0)
@register.filter
def calculate_percentage(value, total):
    if total > 0:
        return (value * 100) / total
    return 0