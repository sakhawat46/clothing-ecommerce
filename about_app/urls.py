from django.conf.urls import url
from django.urls import path
from about_app import views

app_name = "about_app"

urlpatterns = [
    path('', views.about, name='about'),

]