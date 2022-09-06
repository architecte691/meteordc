from django.shortcuts import render, get_object_or_404
from .models import Moment, City
from blog.models import Annonce
from datetime import datetime, date

# Create your views here.


def home(request):
    actu = datetime.today()
    moments = Moment.objects.filter(date_actu=actu).order_by('city__name')
    annonces = Annonce.objects.order_by('-id')
    return render(request, 'main/home.html', locals())


def cities(request):
    actu = datetime.today()
    moments = Moment.objects.filter(date_actu=actu).order_by('city__name')
    return render(request, 'main/cities.html', locals())


def city_detail(request, identify):
    actu = datetime.today()
    ville = City.objects.get(name=identify)
    moments = Moment.objects.filter(city__name=ville.name).order_by('date_actu')
    return render(request, 'main/city_detail.html', locals())


def news(request):
    moments = Moment.objects.filter(city__name='kinshasa')
    return render(request, 'main/news.html', locals())
