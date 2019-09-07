from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(OLM)
admin.site.register(Region)
admin.site.register(Zone)