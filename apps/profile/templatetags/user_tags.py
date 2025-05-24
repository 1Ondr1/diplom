from django import template
from apps.profile.utils import is_user_online

register = template.Library()

@register.simple_tag
def check_user_online(user):
    return is_user_online(user)
