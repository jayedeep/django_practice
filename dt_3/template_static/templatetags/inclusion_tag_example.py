import datetime
from django import template

register = template.Library()
@register.inclusion_tag("sublist.html")
def include_list(iterator):
    return {"iterator": iterator}