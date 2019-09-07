from django.urls import path
from . import views

urlpatterns = [
    path('type/<statut>/', views.ActivitesR.as_view(), name='Activite'),
    path("details/activite/<id>/", views.DetailsR.as_view(), name="details_actvr"),
]