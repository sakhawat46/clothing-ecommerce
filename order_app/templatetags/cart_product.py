from atexit import register
from django import template
from order_app.models import Cart, Order

register = template.Library()

@register.filter
def cart_view(request):
    cart = Cart.objects.filter(user=request.COOKIES['device'], purchased=False)
    if cart.exists():
        return cart
    else:
        return cart


@register.filter
def cart_total(request):
    order = Order.objects.filter(user=request.COOKIES['device'], ordered=False)
    if order.exists():
        return order[0].get_totals()
    else:
        return 0

@register.filter
def cart_count(request):
    order = Order.objects.filter(user=request.COOKIES['device'], ordered=False)
    if order.exists():
        return order[0].orderitems.count()
    else:
        return 0