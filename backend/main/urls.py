from django.urls import path
from .views import home, city_detail, news
urlpatterns = [
    path('', home, name='home'),
    path('detail_ville/<int:identify>', city_detail, name='city_detail'),
    path('annonces', news, name='news'),
]