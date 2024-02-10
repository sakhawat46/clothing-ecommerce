from django.conf.urls import url
from django.urls import path
from store_app import views

app_name = "store_app"

urlpatterns = [
    path('', views.HomeListView.as_view(), name='index'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product_details'),
    path('category/<slug:slug>/', views.category_details, name='category_details'),
    path('shop/', views.ShopListView.as_view(), name='shop'),

]