from django import template
from portal.models import User

register = template.Library()

@register.filter
def userkarma(value):
   u = User.objects.get(id=value)
   return u.get_karma()


@register.filter
def cut(value, arg):
   """Removes all values of arg from the given string"""
   return value.replace(arg, '')
