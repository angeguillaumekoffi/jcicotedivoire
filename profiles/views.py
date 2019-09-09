from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from Activites.models import *
from actualites.models import *
from . import forms
from . import models


class ShowProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/show_profile.html"
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get("slug")
        if slug:
            profile = get_object_or_404(models.Profile, slug=slug)
            user = profile.user
        else:
            user = self.request.user

        if user == self.request.user:
            kwargs["editable"] = True

        util = self.request.user
        prof = get_object_or_404(models.Profile, user=user)
        pub = models.Publications.objects.filter(pub_par=prof).order_by('pub_dat').reverse()[:4]
        publi = models.Publications.objects.all().order_by('pub_dat').reverse()
        actua = Actualites.objects.all().order_by('-actu_dat')[:8]
        activ = Activites.objects.all().order_by('-date_pub')[:15]
        kwargs["Actua"] = actua
        kwargs["Activ"] = activ
        kwargs["show_user"] = user
        kwargs["publication"] = pub
        kwargs["publi"] = publi
        return super().get(request, *args, **kwargs)


class EditProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/edit_profile.html"
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if "user_form" not in kwargs:
            kwargs["user_form"] = forms.UserForm(instance=user)
        if "profile_form" not in kwargs:
            kwargs["profile_form"] = forms.ProfileForm(instance=user.profile)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        user_form = forms.UserForm(request.POST, instance=user)
        profile_form = forms.ProfileForm(
            request.POST, request.FILES, instance=user.profile
        )
        if not (user_form.is_valid() and profile_form.is_valid()):
            messages.error(
                request,
                "Echec de validadation ! " "Revoyez les details s'il vous plait.",
            )
            user_form = forms.UserForm(instance=user)
            profile_form = forms.ProfileForm(instance=user.profile)
            return super().get(request, user_form=user_form, profile_form=profile_form)
        # Both forms are fine. Time to save!
        user_form.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        messages.success(request, "Modifications enregistrées!")
        return redirect("profiles:show_self")

class Posts(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/post.html"
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get("slug")
        if slug:
            profile = get_object_or_404(models.Profile, slug=slug)
            user = profile.user
        else:
            user = self.request.user

        if user == self.request.user:
            kwargs["show_user"] = user
        prof = get_object_or_404(models.Profile, user=user)
        auteur = models.Publications(pub_par=prof)
        pub_form = forms.PublicationsForm(instance=auteur)
        return super().get(request, form=pub_form, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        pub_form = forms.PublicationsForm(request.POST, request.FILES)
        if not (pub_form.is_valid()):
            messages.error(
                request,
                "Echec de validadation ! " "Revoyez les details s'il vous plait.",
            )
            user_form = forms.UserForm(instance=user)
            profile_form = forms.ProfileForm(instance=user.profile)
            prof = get_object_or_404(models.Profile, user=user)
            auteur = models.Publications(pub_par=prof)
            pub_form = forms.PublicationsForm(instance=auteur)
            return super().get(request, user_form=user_form, profile_form=profile_form, form=pub_form)

        prof = models.Profile.objects.get(user=user)
        auteur = models.Publications(pub_par=prof)
        donnees = pub_form.save(commit=False)
        donnees.pub_par = auteur.pub_par
        donnees.save()
        messages.success(request, "publié !")
        return redirect("profiles:show_self")
            
class Formulaire(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/formulaire.html"
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if "user_form" not in kwargs:
            kwargs["user_form"] = forms.UserForm(instance=user)
        if "profile_form" not in kwargs:
            kwargs["profile_form"] = forms.Formulaire(instance=user.profile)

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        user_form = forms.UserForm(request.POST, instance=user)
        profile_form = forms.Formulaire(
            request.POST, request.FILES, instance=user.profile
        )
        if not (profile_form.is_valid()):
            messages.error(
                request,
                "Echec de validadation ! " "Revoyez les details s'il vous plait.",
            )
            user_form = forms.UserForm(instance=user)
            profile_form = forms.Formulaire(instance=user.profile)
            return super().get(request, user_form=user_form, profile_form=profile_form)
        # Both forms are fine. Time to save!
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        messages.success(request, "Félicitation! Il ne reste plus qu'une étape à valider")
        return redirect("profiles:formation")

class Formation(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/formation.html"
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if "profile_form" not in kwargs:
            kwargs["profile_form"] = forms.FormationForm(instance=user.profile)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        profile_form = forms.FormationForm(request.POST, request.FILES)
        if not (profile_form.is_valid()):
            messages.error(
                request,
                "Echec de validadation ! " "Revoyez les details s'il vous plait.",
            )
            profile_form = forms.FormationForm(instance=user.profile)
            return super().get(request, profile_form=profile_form)
        # Both forms are fine. Time to save!
        prof = models.Profile.objects.get(user=user)
        auteur = models.Formation(adherant=prof)
        profile = profile_form.save(commit=False)
        profile.adherant = auteur.adherant
        profile.save()
        messages.success(request, "Félicitation {} vous povez ajouter autant de formations que vous en avez!".format(profile.adherant.user.name))
        return redirect("profiles:formation")
