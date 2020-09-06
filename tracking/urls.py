from django.urls import include, path

from tracking.views import tracking,business,individual


urlpatterns = [
    path('', tracking.home, name='home'),


]
