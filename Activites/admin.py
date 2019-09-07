from django.contrib import admin# Register your models here.
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import *

class bande(GenericTabularInline):
    model = BandeInfo

class BD(admin.ModelAdmin):
    inlines = [
        bande
    ]

admin.site.register(Activites)
admin.site.register(Statut_Activite)