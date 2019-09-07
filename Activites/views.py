from django.shortcuts import render, redirect, get_object_or_404
from django.forms import formset_factory
from django.views import generic
from django.contrib import messages
from OLM.models import OLM
from Activites.models import *
from actualites.models import *
from actualites.forms import *
from profiles.models import Publications
from Presidents.models import *

# Create your views here.
class ActivitesR(generic.TemplateView):
    template_name = 'pages/activ_realise.html'
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        activ = Activites.objects.filter(statut_actv=kwargs["statut"]).order_by('-date_pub')
        actua_gal = Actualites.objects.all().order_by('-actu_dat')[:4]
        publi_gal = Publications.objects.all().order_by('-pub_dat')[:4]
        List_olm = OLM.objects.all().order_by('olm')
        Bande_info = BandeInfo.objects.all().order_by('-id')
        if "abn_form" not in kwargs:
            kwargs["abn_form"] = AbonnesForm()
        kwargs["stat"] = kwargs["statut"]
        kwargs["List_olm"] = List_olm
        kwargs["Info"] = Bande_info
        kwargs["Activ"] = activ
        kwargs["Publi_gal"] = publi_gal
        kwargs["Actua_gal"] = actua_gal
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        abn_form = AbonnesForm(request.POST)
        if abn_form.is_valid():
            try:
                abn_form.save()
                messages.success(request, "merci de vous etes abonné!")
                return redirect("home")
            except:
                messages.error(
                    request,
                    "Echec de validadation ! " "Revoyez les details s'il vous plait.", )
                return redirect("home")
        Abn_form = AbonnesForm()
        return super().get(request, abn_form=Abn_form)

    class Details_pub(generic.TemplateView):
        template_name = 'pages/publi_membre.html'
        http_method_names = ["get", "post"]

        def get(self, request, *args, **kwargs):
            detail_publi = get_object_or_404(Publications, id=kwargs["id"])
            actua_gal = Actualites.objects.all().order_by('-actu_dat')[:4]
            publi_gal = Publications.objects.all().order_by('-pub_dat')[:4]
            List_olm = OLM.objects.all().order_by('olm')
            Bande_info = BandeInfo.objects.all().order_by('-id')
            if "cont_form" not in kwargs:
                kwargs["cont_form"] = ContactForm()
            if "abn_form" not in kwargs:
                kwargs["abn_form"] = AbonnesForm()
            kwargs["detail_publi"] = detail_publi
            kwargs["List_olm"] = List_olm
            kwargs["Info"] = Bande_info
            kwargs["Publi_gal"] = publi_gal
            kwargs["Actua_gal"] = actua_gal
            return super().get(request, *args, **kwargs)

        def post(self, request, *args, **kwargs):
            abn_form = AbonnesForm(request.POST)
            if abn_form.is_valid():
                try:
                    abn_form.save()
                    messages.success(request, "merci de vous etes abonné!")
                    return redirect("home")
                except:
                    messages.error(
                        request,
                        "Echec de validadation ! " "Revoyez les details s'il vous plait.", )
                    return redirect("home")
            Abn_form = AbonnesForm()
            return super().get(request, abn_form=Abn_form)

class DetailsR(generic.TemplateView):
    template_name = 'pages/activR_details.html'
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
            detail = get_object_or_404(Activites, titre=kwargs["id"])
            actua_gal = Actualites.objects.all().order_by('-actu_dat')[:4]
            publi_gal = Publications.objects.all().order_by('-pub_dat')[:4]
            List_olm = OLM.objects.all().order_by('olm')
            Bande_info = BandeInfo.objects.all().order_by('-id')
            if "cont_form" not in kwargs:
                kwargs["cont_form"] = ContactForm()
            if "abn_form" not in kwargs:
                kwargs["abn_form"] = AbonnesForm()
            kwargs["detail_actv"] = detail
            kwargs["List_olm"] = List_olm
            kwargs["Info"] = Bande_info
            kwargs["Publi_gal"] = publi_gal
            kwargs["Actua_gal"] = actua_gal
            return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
            abn_form = AbonnesForm(request.POST)
            if abn_form.is_valid():
                try:
                    abn_form.save()
                    messages.success(request, "merci de vous etes abonné!")
                    return redirect("home")
                except:
                    messages.error(
                        request,
                        "Echec de validadation ! " "Revoyez les details s'il vous plait.", )
                    return redirect("home")
            Abn_form = AbonnesForm()
            return super().get(request, abn_form=Abn_form)