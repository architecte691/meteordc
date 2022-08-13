from django.urls import path
from .views import connect 
urlpatterns = [
    path('connexion', connect, name='connect'),
    path('disconnect', connect, name='disconnect'),
    path('profile', connect, name='profile'),
    path('subscription', connect, name='subscription'),
]