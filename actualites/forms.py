from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field, Column
from .models import Contact, Abonnes

class ContactForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field("cont_nom"),
            Field("cont_mail"),
            Field("cont_obj"),
            Field("cont_msg"),

            Submit("update", "Envoyer", css_class="btn-warning"),
        )
    class Meta:
        model = Contact
        fields = ["cont_nom", "cont_mail", "cont_obj", "cont_msg"]


class AbonnesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("Abn_mail", placeholder="Adresse mail"), )
    class Meta:
        model = Abonnes
        fields = '__all__'