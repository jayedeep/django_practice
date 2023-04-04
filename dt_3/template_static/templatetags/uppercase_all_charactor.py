from django import template

register = template.Library()

@register.filter()
def uppercase_all_charactor(string):
    print("Uppercase all characters",string)
    return string.upper()