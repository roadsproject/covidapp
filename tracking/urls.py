from django.urls import include, path

from tracking.views import tracking


urlpatterns = [
    path('', tracking.home, name='home'),


]
