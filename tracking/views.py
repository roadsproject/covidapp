from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import UserForm, SigninForm,VisitForm
from .models import User,Visit,Business
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from .models import Visit
from .filters import UserFilter, CheckFilter





def home(request):
    businesslist = Business.objects.order_by('-business_name')
    return render(request, 'tracking/home.html', {'business': businesslist})

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'tracking/signupuser.html', {'form': UserForm()})
    else:
        if request.POST['password'] == request.POST['password_confirm']:
            try:
                form = UserForm(request.POST)
                user = form.save(commit=False)
                password = form.cleaned_data['password']
                user.set_password(password)
                user.save()
                return redirect('home')
            except:
                return render(request, 'tracking/signupuser.html', {'form': UserForm(),
                                                                'error': 'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'tracking/signupuser.html', {'form': UserForm(), 'error': 'Username and password did not match'})

def businesspage(request, business_id):
    business = get_object_or_404(Business, pk=business_id)
    return render(request, 'tracking/business.html', {'business': business})

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def check_admin(user):
   return user.is_staff

@user_passes_test(check_admin)
def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'tracking/user_list.html', {'filter': user_filter})


@user_passes_test(check_admin)
def checkinsearch(request):
    checkin = Visit.objects.order_by('-datetime')
    checkin_filter = CheckFilter(request.GET, queryset=checkin)
    user_list = User.objects.all()
    return render(request, 'tracking/checkin_list.html', {'filter': checkin_filter})


class CreateBusinessView(CreateView):
    model = Business
    template_name = 'tracking/createbusiness.html'
    fields = ('business_name','contact_name','email','phone')
    success_url = reverse_lazy('home')

@method_decorator(login_required,name='dispatch')
class VisitView(CreateView):
    model = Visit
    form_class = VisitForm
    success_url = reverse_lazy('home')
    template_name = 'tracking/visit.html'


    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user
        self.object.save()

        return super(VisitView, self).form_valid(form)

@method_decorator(login_required,name='dispatch')
class VisitListView(ListView):
    model = Visit
    context_object_name = 'visit'
    paginate_by = 10





    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user
        self.object.save()

        return super(VisitView, self).form_valid(form)
