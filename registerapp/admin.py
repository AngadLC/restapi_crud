from django.contrib import admin
from .models import registermodel
# Register your models here.
from django.contrib import admin
from .models import registermodel

@admin.register(registermodel)
class registermodelAdmin(admin.ModelAdmin):
     list_display = ('name', 'password', 'email')