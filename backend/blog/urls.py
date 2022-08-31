from django.urls import path
from .views import index
urlpatterns = [
    path('/annonces', index, name='blog'),
]
