"""covidapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from tracking import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),



    path('signup/', views.signupuser, name='signupuser'),
    path('login/', auth_views.LoginView.as_view(template_name='tracking/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='tracking/logout.html'), name='logoutuser'),
    #path('visit/', views.VisitView.as_view(),name ='visit'),
    path('visit/', views.VisitView.as_view(), name='visit'),
    path('createbusiness/', views.CreateBusinessView.as_view(), name='createbusiness'),



    path('', views.home, name='home'),

]
