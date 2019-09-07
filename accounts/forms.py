from __future__ import unicode_literals
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field
from authtools import forms as authtoolsforms
from django.contrib.auth import forms as authforms
from django.urls import reverse


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, initial=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["username"].widget.input_type = "email"  # ugly hack

        self.helper.layout = Layout(
            Field("username", placeholder="Entrer Email", autofocus=""),
            Field("password", placeholder="Entrer Mot de passe"),
            HTML(
                '<a href="{}">Mot de passe oublié?</a>'.format(
                    reverse("accounts:password-reset")
                )
            ),
            Field("remember_me", verbose_name="Memoriser ma session" ),
            Submit("sign_in", "Connexion", css_class="btn btn-lg btn-primary btn-block"),
        )


class SignupForm(authtoolsforms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["email"].widget.input_type = "email"  # ugly hack
        self.helper.layout = Layout(
            Field("email", placeholder="Entrer Email", autofocus=""),
            Field("name", placeholder="Nom d'utilisateur"),
            Field("password1", placeholder="Entrer Mot de passe"),
            Field("password2", placeholder="Entrer Mot de passe (Encore)"),
            Submit("sign_up", "Suivant", css_class="btn-large"),
        )


class PasswordChangeForm(authforms.PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field("old_password", placeholder="Entrer ancien Mot de passe", autofocus=""),
            Field("new_password1", placeholder="Entrer nouveau Mot de passe"),
            Field("new_password2", placeholder="Entrer nouveau Mot de passe (Encore)"),
            Submit("pass_change", "Changer", css_class="btn-warning"),
        )


class PasswordResetForm(authtoolsforms.FriendlyPasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field("email", placeholder="Entrer email", autofocus=""),
            Submit("pass_reset", "Reinitialiser", css_class="btn-warning"),
        )


class SetPasswordForm(authforms.SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field("new_password1", placeholder="Entrer un Mot de passe", autofocus=""),
            Field("new_password2", placeholder="Entrer Mot de passe (encore)"),
            Submit("pass_change", "Valider", css_class="btn-warning"),
        )
