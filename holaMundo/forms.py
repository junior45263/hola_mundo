# myapp/forms.py
from django import forms
from .models import UserProfile


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password']
        widgets = {'password': forms.PasswordInput()}

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    next = forms.CharField(widget=forms.HiddenInput, initial='/holaMundo/home/')
    