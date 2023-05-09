from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('demo/', views.demo, name = 'demo'),
    path('showform/', views.show_form, name = 'show_form'),
    path('showform/getform', views.get_form, name = 'get_form')
]
