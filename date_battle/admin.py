from django.contrib import admin
#Use this when time comes to create an abstract user
#from django.contrib.auth.models import AbstractUser
from .models import Challenge, Entries
# Register your models here.
admin.site.register(Challenge)
admin.site.register(Entries)

