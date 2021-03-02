from django import template

register = template.Library()

# Splits string into a list
@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return str(value).split(key)