from django import forms

class RegisterForm(forms.Form):
    identifiant = forms.CharField(label='Identifiant', widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password    = forms.CharField(label='Mot de Passe', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

class LoginForm(forms.Form):
    identifiant = forms.CharField(label='Identifiant', widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password    = forms.CharField(label='Mot de Passe', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
