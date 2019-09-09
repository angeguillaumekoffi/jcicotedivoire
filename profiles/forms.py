from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth import get_user_model
from profiles.models import *

User = get_user_model()


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field("name"),
            Field("email")
            )

    class Meta:
        model = User
        fields = ["name", "email"]


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field("bio"),
            Field("picture"),
            Field("prof"),
            Field("tel"),
            Field("bp"),
            Submit("update", "Valider", css_class="btn-warning"),
        )

    class Meta:
        model = Profile
        fields = ["bio","picture","prof","tel","bp"]

class ImgForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field("picture"),
            Submit("update", "Valider", css_class="btn-warning"),
        )
    class Meta:
        model = Profile
        fields = ["picture"]


class PublicationsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Field("pub_file"),
            Field("pub_text"),
            Submit("update", "Publier", css_class="btn-large"),
        )
    class Meta:
        model = Publications
        fields = ("pub_par", "pub_file", "pub_text")

class FormationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Field("theme"),
            Field("forma_dat"),
            Field("formateur"),
            Submit("update", "Valider", css_class="btn-large"),
        )
    class Meta:
        model = Formation
        fields = ("adherant", "theme", "forma_dat", "formateur")

class Formulaire(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field("olm"),
            Field("nom_pren"),
            Field("Datn"),
            Field("Sit_matri"),
            Field("conjoint"),
            Field("prof"),
            Field("employ"),
            Field("tel"),
            Field("bp"),
            Field("dat_pc"),
            Field("commiss"),
            Field("par_mar"),
            Field("actv_loc"),
            Field("actv_zon"),
            Field("actv_nat"),
            Field("actv_inter"),
            Submit("update", "Valider", css_class="btn-large"),
        )
    class Meta:
        model = Profile
        fields = ["olm","nom_pren","Datn","Sit_matri","conjoint","prof","employ","tel","bp","dat_pc",
            "commiss","par_mar","actv_loc","actv_zon","actv_nat","actv_inter"]
