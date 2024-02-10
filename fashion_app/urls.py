from django.conf.urls import url
from django.urls import path
from fashion_app import views

app_name = "fashion_app"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.customerlogin, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

]