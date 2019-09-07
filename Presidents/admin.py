from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(DonneesPresi)
admin.site.register(Institutions)
admin.site.register(Plan)