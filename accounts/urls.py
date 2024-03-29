from django.urls import path
from django.conf.urls import url

from . import views

app_name = "accounts"
urlpatterns = [
    path("connexion/", views.LoginView.as_view(), name="login"),
    path("deconnexion/", views.LogoutView.as_view(), name="logout"),
    path("inscription/", views.SignUpView.as_view(), name="signup"),
    path("changer-mot-de-passe", views.PasswordChangeView.as_view(), name="password-change"
    ),
    path("password-reset/", views.PasswordResetView.as_view(), name="password-reset"),
    path(
        "password-reset-done/",
        views.PasswordResetDoneView.as_view(),
        name="password-reset-done",
    ),
    url(
        r"^password-reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$",
        views.PasswordResetConfirmView.as_view(),
        name="password-reset-confirm",
    ),
]
