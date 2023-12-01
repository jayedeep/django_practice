from django import template

register = template.Library()

@register.simple_tag
def change_city(value):
    print(value,"????????????????\n\n\n\n")
    return value.title()