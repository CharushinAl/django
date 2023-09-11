from django import template

register = template.Library()


@register.filter(name='media_path')
def media_path(value):
    if value:
        return f'media/products/{value}'
    return '#'


@register.simple_tag(name='media_path')
def media_path(value):
    if value:
        return f'media/products/{value}'
    return '#'
