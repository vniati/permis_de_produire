from django import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class MyRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = [
        User.USERNAME_FIELD,
        'password1',
        'password2'
        ]
        required_css_class = 'required'



# class RegisterForm(forms.Form):
#     identifiant = forms.CharField(label='Identifiant', widget=forms.TextInput(attrs={'class' : 'form-control'}))
#     password    = forms.CharField(label='Mot de Passe', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
# 
# class LoginForm(forms.Form):
#     identifiant = forms.CharField(label='Identifiant', widget=forms.TextInput(attrs={'class' : 'form-control'}))
#     password    = forms.CharField(label='Mot de Passe', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
