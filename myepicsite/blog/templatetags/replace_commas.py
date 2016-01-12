from django import template

register = template.Library()

@register.filter
def stringify(value): 
    return str(value)
