from django.shortcuts import render

# Create your views here.


def connect(request):
    return render(request, 'users/connect.html')


def disconnect(request):
    return render(request, 'users/disconnect.html')


def profile(request):
    return render(request, 'users/profile.html')


def subscription(request):
    return render(request, 'users/subscription.html')
