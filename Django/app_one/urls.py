from django.urls import path
from . import views
from . import forms

urlpatterns = [
    path('', views.home, name='home'),
    path('demo/', views.demo, name = 'demo'),
    path('showform/', views.show_form, name = 'show_form'),
    path('showform/getform', views.get_form, name = 'get_form'),
    path('dish/<str:name>', views.dish, name = 'dish'),
    path('index/', views.index, name = 'index'),
    path('index/getindex', views.get_index, name = 'get_index'),
]
