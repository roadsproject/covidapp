from django import forms
from django.forms import ModelForm
from .models import User,Visit

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'password']


class SigninForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class VisitForm(ModelForm):
    class Meta:
        model = Visit
        fields = ['business_id','is_in']
