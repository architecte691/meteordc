from django.shortcuts import render, get_object_or_404
from .models import Moment, City

# Create your views here.
def home(request):
    cities = City.objects.order_by('name')
    return render(request,'main/home.html', locals())

def city_detail(request, identify):
    ville = City.objects.get(id=identify)
    moments = Moment.objects.filter(city__name=ville.name)
    return render(request,'main/city_detail.html', locals())

def news(request):
    moments = Moment.objects.filter(city__name='kinshasa')
    return render(request,'main/news.html', locals())
