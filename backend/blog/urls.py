from django.urls import path
from .views import annonce, index
urlpatterns = [
    path('/annonces', index, name='blog'),
    path('/blog/<int:id>', annonce, name="annonce"),
]
