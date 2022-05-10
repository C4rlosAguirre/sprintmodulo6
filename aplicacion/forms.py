from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from aplicacion.models import Cliente

from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre','apellido','edad', 'email', 'fecha_contratacion')

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmacion contraseña", widget=forms.PasswordInput)


class Meta:
    model = User
    fields = ['username', 'email', 'password', 'password2']
    help_texts = {k:"" for k in fields}
