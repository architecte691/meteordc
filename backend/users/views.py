
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from users.forms import ConnexionForm

# Create your views here.


def connect(request):
    url, redirect_url = request.path, request.GET.get('next', '')
    url = url + '?next=' + redirect_url
    print('_______________connect____________')
    print(redirect_url)
    clien = request.method
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            # Nousrécupérons le nom d'utilisateur
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]  # ... et le motde passe
            # Nous vérifions si les données sont correctes
            user = authenticate(username=username, password=password)
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectonsl'utilisateur
                # return redirect('/account/')
                if redirect_url:
                    return redirect(redirect_url)
                return redirect(reverse('home'))
            else:  # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'users/connect.html', locals())


def disconnect(request):
    logout(request)
    return redirect(reverse('connect'))


@login_required(login_url='connect')
def profile(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        data = request.POST
        print(data)
        for name, value in data.items():
            if name in ['email', 'username', 'first_name', 'last_name', 'new_profil_avatar']:
                print(name)
                if name == 'new_profil_avatar':
                    print('file in data _________')
                    print(value)
                    user.avatar.save(value.name, value, save=True)
                else:
                    vars(user)[name] = value
                user.save()

    request.user = user

    return render(request, 'users/profile.html')


def subscription(request):
    return render(request, 'users/subscription.html')
