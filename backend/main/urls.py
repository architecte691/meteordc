from django.urls import path
from .views import home, city_detail, news, cities
urlpatterns = [
    path('', home, name='home'),
    path('villes', cities, name='cities'),
    path('detail_ville/<str:identify>', city_detail, name='city_detail'),
    path('annonces', news, name='news'),
]
