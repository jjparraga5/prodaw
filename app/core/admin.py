from django.contrib import admin

# Register your models here.
from .models import Employe, Type

admin.site.register(Employe)
admin.site.register(Type)
