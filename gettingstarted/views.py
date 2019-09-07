from django.shortcuts import redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from OLM.models import OLM
from Activites.models import BandeInfo, Activites
from actualites.models import *
from actualites.forms import *
from profiles.models import Publications, Profile
from Presidents.models import *


class PresidentsView(generic.TemplateView):
    template_name = 'pages/presidents.html'
    http_method_names=["get", "post"]

    def get(self, request, *args, **kwargs):
        actua_gal = Actualites.objects.all().order_by('-actu_dat')[:4]
        publi_gal = Publications.objects.all().order_by('-pub_dat')[:4]
        List_olm = OLM.objects.all().order_by('olm')
        Bande_info = BandeInfo.objects.all().order_by('-id')
        kwargs["List_olm"] = List_olm
        kwargs["Info"] = Bande_info
        kwargs["Publi_gal"] = publi_gal
        kwargs["Actua_gal"] = actua_gal
        presi = DonneesPresi.objects.all().order_by("mdt")
        if "abn_form" not in kwargs:
            kwargs["abn_form"] = AbonnesForm()
        kwargs["President"] = presi
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

class index(generic.TemplateView):
    template_name= 'pages/index.html'
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        actua = Actualites.objects.all().order_by('-actu_dat')[:4]
        actua_gal = Actualites.objects.all().order_by('-actu_dat')[:4]
        publi_gal = Publications.objects.all().order_by('-pub_dat')[:4]
        Actu_sec = Actualites.objects.get(id=1)
        Actu_3 = Actualites.objects.get(id=2)
        List_olm = OLM.objects.all().order_by('olm')
        Bande_info = BandeInfo.objects.all().order_by('-id')
        publi = Publications.objects.all().order_by('-pub_dat')[:4]
        if "cont_form" not in kwargs:
            kwargs["cont_form"]= ContactForm()
        if "abn_form" not in kwargs:
            kwargs["abn_form"] = AbonnesForm()
        kwargs["List_olm"]=List_olm
        kwargs["Info"]=Bande_info
        kwargs["Actu_3"] = Actu_3
        kwargs["Actu_sec"] = Actu_sec
        kwargs["Publi"] = publi
        kwargs["Actua"] = actua
        kwargs["Publi_gal"] = publi_gal
        kwargs["Actua_gal"] = actua_gal
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        cont_form = ContactForm(request.POST)
        abn_form = AbonnesForm(request.POST)
        if cont_form.is_valid():
            try:
                cont_form.save()
                messages.success(request, "Messga envoyé!")
                return redirect("home")
            except:
                messages.error(
                    request,
                        "Echec de validadation ! " "Revoyez les details s'il vous plait.", )
                return redirect("home")
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

        Cont_form = ContactForm()
        Abn_form = AbonnesForm()
        return  super().get(request,  cont_form = Cont_form, abn_form=Abn_form)

class Details(generic.TemplateView):
    template_name = 'pages/image-post.html'
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        detail_actu = get_object_or_404(Actualites, actu_titre=kwargs["titre"])
        actua_gal = Actualites.objects.all().order_by('-actu_dat')[:4]
        publi_gal = Publications.objects.all().order_by('-pub_dat')[:4]
        actua = Actualites.objects.all().order_by('-actu_dat')[:4]
        List_olm = OLM.objects.all().order_by('olm')
        Bande_info = BandeInfo.objects.all().order_by('-id')
        publi = Publications.objects.all().order_by('-pub_dat')[:4]
        if "cont_form" not in kwargs:
            kwargs["cont_form"]= ContactForm()
        if "abn_form" not in kwargs:
            kwargs["abn_form"] = AbonnesForm()
        kwargs["detail_actu"]= detail_actu
        kwargs["List_olm"]=List_olm
        kwargs["Info"]=Bande_info
        kwargs["Publi"] = publi
        kwargs["Actua"] = actua
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
            kwargs["cont_form"]= ContactForm()
        if "abn_form" not in kwargs:
            kwargs["abn_form"] = AbonnesForm()
        kwargs["detail_publi"] = detail_publi
        kwargs["List_olm"]=List_olm
        kwargs["Info"]=Bande_info
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

class ActualitesView(generic.TemplateView):
    template_name = 'pages/Actualites.html'
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        actua = Actualites.objects.all().order_by('-actu_dat')[:10]
        actua_gal = Actualites.objects.all().order_by('-actu_dat')[:4]
        publi_gal = Publications.objects.all().order_by('-pub_dat')[:4]
        List_olm = OLM.objects.all().order_by('olm')
        Bande_info = BandeInfo.objects.all().order_by('-id')
        publi = Publications.objects.all().order_by('-pub_dat')[:10]
        if "cont_form" not in kwargs:
            kwargs["cont_form"] = ContactForm()
        if "abn_form" not in kwargs:
            kwargs["abn_form"] = AbonnesForm()
        kwargs["List_olm"] = List_olm
        kwargs["Info"] = Bande_info
        kwargs["Publi"] = publi
        kwargs["Actua"] = actua
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

class About(generic.TemplateView):
    template_name = 'pages/about.html'
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        actua_gal = Actualites.objects.all().order_by('-actu_dat')[:4]
        publi_gal = Publications.objects.all().order_by('-pub_dat')[:4]
        List_olm = OLM.objects.all().order_by('olm')
        Bande_info = BandeInfo.objects.all().order_by('-id')
        institut = Institutions.objects.all()
        kwargs["List_olm"] = List_olm
        kwargs["Info"] = Bande_info
        kwargs["institut"] = institut
        kwargs["Publi_gal"] = publi_gal
        kwargs["Actua_gal"] = actua_gal
        return super().get(request, *args, **kwargs)

class Guide(generic.TemplateView):
    template_name = 'pages/guide.html'
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        actua_gal = Actualites.objects.all().order_by('-actu_dat')[:4]
        publi_gal = Publications.objects.all().order_by('-pub_dat')[:4]
        List_olm = OLM.objects.all().order_by('olm')
        Bande_info = BandeInfo.objects.all().order_by('-id')
        kwargs["List_olm"] = List_olm
        kwargs["Info"] = Bande_info
        kwargs["Publi_gal"] = publi_gal
        kwargs["Actua_gal"] = actua_gal
        return super().get(request, *args, **kwargs)

class Constitution(generic.TemplateView):
    template_name = 'pages/constitution.html'
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        actua_gal = Actualites.objects.all().order_by('-actu_dat')[:4]
        publi_gal = Publications.objects.all().order_by('-pub_dat')[:4]
        List_olm = OLM.objects.all().order_by('olm')
        Bande_info = BandeInfo.objects.all().order_by('-id')
        kwargs["List_olm"] = List_olm
        kwargs["Info"] = Bande_info
        kwargs["Publi_gal"] = publi_gal
        kwargs["Actua_gal"] = actua_gal
        return super().get(request, *args, **kwargs)

class Gallerie(generic.TemplateView):
    template_name = 'pages/Gallerie_photo.html'
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        actua_gal = Actualites.objects.all().order_by('-actu_dat')[:4]
        publi_gal = Publications.objects.all().order_by('-pub_dat')[:4]
        Actua = Actualites.objects.all().order_by("-actu_dat")
        Publi = Publications.objects.all().order_by("-pub_dat")
        Activ = Activites.objects.all().order_by("-date_pub")
        List_olm = OLM.objects.all().order_by('olm')
        Bande_info = BandeInfo.objects.all().order_by('-id')
        kwargs["List_olm"] = List_olm
        kwargs["Info"] = Bande_info
        kwargs["Actua"] = Actua
        kwargs["Publi"] = Publi
        kwargs["Activ"] = Activ
        kwargs["Publi_gal"] = publi_gal
        kwargs["Actua_gal"] = actua_gal
        return super().get(request, *args, **kwargs)

class ResultatRech(generic.TemplateView):
    template_name = 'pages/resulrech.html'

    def get(self, request, *args, **kwargs):
        req = self.request.GET.get('q')
        resultolm = OLM.objects.filter(olm__icontains=req)
        resultuser = Profile.objects.filter(nom_pren__icontains=req)
        actua_gal = Actualites.objects.all().order_by('-actu_dat')[:4]
        publi_gal = Publications.objects.all().order_by('-pub_dat')[:4]
        Activ = Activites.objects.all().order_by("-date_pub")
        List_olm = OLM.objects.all().order_by('olm')
        Bande_info = BandeInfo.objects.all().order_by('-id')
        if "abn_form" not in kwargs:
            kwargs["abn_form"] = AbonnesForm()
        kwargs["result"] = resultolm
        kwargs["resultuser"] = resultuser
        kwargs["List_olm"] = List_olm
        kwargs["Info"] = Bande_info
        kwargs["Activ"] = Activ
        kwargs["Publi_gal"] = publi_gal
        kwargs["Actua_gal"] = actua_gal
        return super().get(request, *args, **kwargs)