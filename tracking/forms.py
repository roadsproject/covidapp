<<<<<<< HEAD

from django import forms
from django.forms import ModelForm
=======
from django.forms import ModelForm
from django import forms
>>>>>>> d3b74ae50949766c59a4e90e2242e48cbfaa42e9
from .models import User

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
<<<<<<< HEAD
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'password']
=======
        fields = ['user_name', 'first_name', 'last_name', 'email', 'phone','password']
>>>>>>> d3b74ae50949766c59a4e90e2242e48cbfaa42e9

class SigninForm(ModelForm):
    class Meta:
        model = User
<<<<<<< HEAD
        fields = ['username', 'password']
=======
        fields = ['user_name', 'password']
>>>>>>> d3b74ae50949766c59a4e90e2242e48cbfaa42e9
