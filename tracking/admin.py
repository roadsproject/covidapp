from django.contrib import admin
from .models import User,Individual,Business
# Register your models here.
admin.site.register(User)
admin.site.register(Business)
#admin.site.register(Visit)
admin.site.register(Individual)
