from django import template

register = template.Library()


@register.filter()
def mymedia(val):
    if val:
        return f'/media/{val}'
    else:
        return '/static/placeholder/dog.png'
