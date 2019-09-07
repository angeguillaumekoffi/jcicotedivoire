from django.contrib import admin
from .models import *
from Activites.models import BandeInfo
# Register your models here.

class ContAdmin(admin.ModelAdmin):
    list_display = ("cont_nom", "cont_mail", "cont_obj", "cont_msg", "cont_dat")
    readonly_fields = ("cont_nom", "cont_mail", "cont_obj", "cont_msg", "cont_dat")

class AbntAdmin(admin.ModelAdmin):
    list_display = ("id", "Abn_dat", "Abn_mail")
    readonly_fields = ("id", "Abn_dat", "Abn_mail")

class ActtAdmin(admin.ModelAdmin):
    list_display = ("id", "actu_titre", "actu_dat")
    readonly_fields = ("id", "actu_dat")


admin.site.register(BandeInfo)
admin.site.register(Actualites, ActtAdmin)
admin.site.register(Contact, ContAdmin)
admin.site.register(Abonnes, AbntAdmin)