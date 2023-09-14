from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.formView, name='Form View'),
]
