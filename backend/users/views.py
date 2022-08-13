from django.shortcuts import render

# Create your views here.
def connect(request):
    return render('users/connect.html')

def disconnect(request):
    return render('users/disconnect.html')

def profile(request):
    return render('users/profile.html')

def subscription(request):
    return render('users/subscription.html')