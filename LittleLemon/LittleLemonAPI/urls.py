from django.urls import path, include
from . import views

urlpatterns = [
    path('books', views.BookList.as_view()),
    path('books/<int:pk>', views.Book.as_view()),
    path('players/', views.players, name='Players'),
    path('players/<int:id>', views.single_player, name='Single Player'),
    path('__debug__/', include('debug_toolbar.urls')),
]