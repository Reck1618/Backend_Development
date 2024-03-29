from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('books', views.BookList.as_view()),
    path('books/<int:pk>', views.Book.as_view()),
    path('players/', views.players, name='Players'),
    path('players/<int:id>', views.single_player, name='single-player'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('teams/<int:id>', views.single_team, name='single-team'),
    path('secret/', views.secret, name='secret'),
    path('api-token-auth/', obtain_auth_token),
    path('manager/', views.manager_view, name='manager'),
    path('throttle-check/', views.throttle_check, name='throttle-check'),
    path('throttle-check-auth/', views.throttle_check_auth, name='throttle-check-auth'),
    path('throttle-check-custom/', views.throttle_check_custom, name='throttle-check-custom'),
    path('players-class/', views.PlayersViewSet.as_view({'get': 'list'})),
    path('players-class/<int:pk>', views.PlayersViewSet.as_view({'get': 'retrieve'})),
    path('groups/manager/users', views.managers, name='managers'),
]