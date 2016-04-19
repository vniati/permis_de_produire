from django import forms

class RegisterForm(forms.Form):
    identifiant = forms.CharField(label='Identifiant', widget=forms.TextInput(attrs={'class' : 'form-control'}),  required=True, max_length=130)
    mot_de_passe = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}), label='Mot de Passe',required=True, max_length=100)
