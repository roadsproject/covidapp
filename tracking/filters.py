from .models import User, Visit
import django_filters
from django import forms

class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'phone', 'email' ]

class CheckFilter(django_filters.FilterSet):
    class Meta:
        model = Visit
        fields = {
            'user_id': ['exact', ],
            'business_id': ['exact', ],
            'record_type': ['exact', ],
            'datetime': ['year','month','day','hour__gt','hour__lt'  ],
        }