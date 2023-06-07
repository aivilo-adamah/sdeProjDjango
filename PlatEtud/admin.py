from django.contrib import admin
from . models import Cour
# Register your models here.
@admin.register(Cour)
class CourModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'titre', 'image']