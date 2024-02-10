from atexit import register
from django import template
from store_app.models import Category

register = template.Library()

@register.filter
def category(user):

    cat = Category.objects.filter(parent=None)
    return cat

    # if user.is_authenticated:
    #     cat = Category.objects.filter(parent=None)
    #     return cat