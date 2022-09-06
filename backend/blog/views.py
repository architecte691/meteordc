from django.shortcuts import render
from blog.models import Annonce

# Create your views here.


def index(request):
    annonces = Annonce.objects.order_by('-id')
    return render(request, 'blog/index.html', locals())

def annonce(request,id):
    return render(request, 'blog/article.html', locals())