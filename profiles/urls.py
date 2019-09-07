from django.urls import path
from . import views

app_name = "profiles"
urlpatterns = [
    path("moi/", views.ShowProfile.as_view(), name="show_self"),
    path("moi/poster/", views.Posts.as_view(), name="poster"),
    path("moi/modifier/", views.EditProfile.as_view(), name="edit_self"),
    path("moi/formulaire/", views.Formulaire.as_view(), name="formulaire"),
    path("moi/formulaire/formations/", views.Formation.as_view(), name="formation"),
    path("<slug:slug>/", views.ShowProfile.as_view(), name="show"),
]
