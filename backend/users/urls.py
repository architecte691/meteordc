from django.urls import path
from .views import connect, profile, disconnect, subscription
urlpatterns = [
    path('/connexion', connect, name='connect'),
    path('/disconnect', disconnect, name='disconnect'),
    path('/profile', profile, name='profile'),
    path('/subscription', subscription, name='subscription'),
    path('/api', subscription, name='api'),
]
