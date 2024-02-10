from django.conf.urls import url
from django.urls import path
from contact_app import views

app_name = "contact_app"

urlpatterns = [
    path('', views.contact, name='contact'),

]