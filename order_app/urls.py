from unicodedata import name
from django.urls import path
from order_app import views

app_name = "order_app"

urlpatterns = [
    path('add-to-cart/<int:pk>/',views.add_to_cart, name='add-to-cart'),
    path('buy_now/<int:pk>/',views.buy_now, name='buy_now'),
    path('cart-view/',views.cart_view, name='cart'),
    path('remove-item/<int:pk>/', views.remove_item_from_cart, name='remove-item'),
    path('increase-quantity/<int:pk>/', views.increase_cart, name='increase'),
    path('decrease-quantity/<int:pk>/', views.decrease_cart, name='decrease'),
]
