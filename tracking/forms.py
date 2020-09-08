from django.forms import ModelForm
from django import forms
from .models import User

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['user_name', 'first_name', 'last_name', 'email', 'phone','password']

class SigninForm(ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'password']
