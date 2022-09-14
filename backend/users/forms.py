
from django.forms import ModelForm
from django import forms
from .models import *


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'first_name', 'last_name']


class ConnexionForm(forms.Form):
    username = forms.CharField(label="E-mail", max_length=50,)
    password = forms.CharField(label="Mot de passe", max_length=50)
