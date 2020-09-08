from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import UserForm, SigninForm
from .models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'tracking/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'tracking/signupuser.html', {'form': UserForm()})
    else:
        if request.POST['password'] == request.POST['password_confirm']:
            try:
                form = UserForm(request.POST)
                user = form.save(commit=False)
                user.save()
                return redirect('home')
            except IntegrityError:
                return render(request, 'tracking/signupuser.html', {'form': UserForm(),
                                                                'error': 'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'tracking/signupuser.html', {'form': UserForm(), 'error': 'Username and password did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'tracking/loginuser.html', {'form':SigninForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'tracking/loginuser.html', {'form':SigninForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')



