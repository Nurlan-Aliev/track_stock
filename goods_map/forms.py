from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'id': 'id_username',
                   'class': 'form-control mb-3',
                   'placeholder': 'username'}))

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={'id': 'id_password',
                   'class': 'form-control mb-3',
                   'placeholder': 'password'}))

    class Meta:
        model = User
        fields = ['name', 'password']
