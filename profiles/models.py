from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from ckeditor.fields import RichTextField
import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone
from OLM.models import OLM
import datetime
choix = [
    ('EN COUPLE', 'en couple'),
    ('CELLIBATAIRE', 'cellibataire'),
    ('DIVORCE(E)', 'divorcé(e)')
]

dat = timezone.now
date = datetime.date.today()

def publication(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'publications/Annee {0}/{1}ieme mois/le {2}/utilisateur_{3}/{4}'.format(date.year, date.month, date.day, instance.pub_par.user.name, filename)

def phot_profile(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'profiles/utilisateur_{0}/{1}/{2}'.format(date, instance.user.name, filename)


class BaseProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, blank=True
    )
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField(
        "Photo de Profile", upload_to=phot_profile, null=True, blank=True
    )
    email_verified = models.BooleanField("Email verifié", default=False)
    olm = models.ForeignKey(OLM, null=True, blank=True, on_delete=models.CASCADE, verbose_name="OLM")
    nom_pren = models.CharField(blank=True, null=True, max_length=100, default="", verbose_name='Nom et Prenoms')
    Datn = models.DateField(blank=True, null=True, verbose_name="Date de naissance")
    Sit_matri = models.CharField(blank=True, max_length=13, default="Cellibataire", choices=choix, verbose_name="Situation matrimoniale")
    conjoint = models.CharField(blank=True, max_length=100, null=True, verbose_name="Conjoint(e)")
    prof = models.CharField(blank=True, max_length=20, null=True, verbose_name="Profession")
    employ = models.CharField(max_length=50, null=True, blank=True, verbose_name="Employeur")
    tel = models.CharField(blank=True, null=True, max_length=30, verbose_name="Tel/Cel")
    bp = models.CharField(max_length=20, blank=True, null=True, verbose_name="Boite postale")
    dat_pc = models.DateField(blank=True, null=True, default=dat, verbose_name="Date de Prise de contact")
    commiss = models.PositiveIntegerField(blank=True,null=True, verbose_name="commission")
    par_mar = models.CharField(blank=True, max_length=50, verbose_name="Parrain/marraine")
    actv_loc = models.CharField(blank=True,null=True, max_length=300, verbose_name="Activites locales")
    actv_zon = models.CharField(blank=True,null=True, max_length=300, verbose_name="Activites zonales")
    actv_nat = models.CharField(blank=True,null=True, max_length=300, verbose_name="Activites nationales")
    actv_inter = models.CharField(blank=True,null=True, max_length=200, verbose_name="Activites internationales")
    bio = models.CharField("Bio", max_length=200, blank=True, null=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Profile(BaseProfile):
    def __str__(self):
        return "{0}".format(self.user.name)

class Publications(models.Model):
    pub_par = models.ForeignKey(Profile, verbose_name=("auteur"), on_delete=models.CASCADE, blank=True, null=True)
    pub_dat = models.DateTimeField("Publié le", auto_now=True)
    pub_text = RichTextField("Contenu", null=True, blank=True)
    pub_file = models.FileField("Choisir une image", upload_to=publication, null=True, blank=True)
    pub_like = models.IntegerField("Likes", null=True, blank=True)
    def __str__(self):
        return "Publié le {0} par {1}".format(self.pub_dat, self.pub_par)

class Formation(models.Model):
    adherant = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Adherant", blank=True)
    theme = models.CharField("Theme", null=True, max_length=100)
    forma_dat = models.DateField("Dates", null=True)
    formateur = models.CharField("Formateurs", null=True, max_length=100)
    def __str__(self):
        return '%s ) %s : %s' %(self.id, self.adherant, self.theme)
    class Meta:
        db_table="Formations"