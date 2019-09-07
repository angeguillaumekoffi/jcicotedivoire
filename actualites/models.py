from django.db import models
import datetime
from ckeditor.fields import RichTextField

# Create your models here.
date = datetime.date.today()

Actu ='Actualites/Annee {0}/{1}ieme mois/le {2}/'.format(date.year, date.month, date.day)

class Actualites(models.Model):
    actu_titre = models.CharField("Titre", max_length=256, blank=True, null=True)
    actu_img = models.ImageField("Image", null=True, blank=True, upload_to=Actu)
    actu_descri = RichTextField("Description", blank=True, null=True)
    actu_dat = models.DateTimeField("Date de publication", auto_now=True)
    class Meta:
        db_table= "Actualites"
    def __str__(self):
        return "{0} | {1}".format(self.actu_dat, self.actu_titre)

class Contact(models.Model):
    cont_nom= models.CharField("Nom" ,max_length=40)
    cont_mail = models.EmailField("Email")
    cont_obj = models.CharField("Objet" ,max_length=250)
    cont_msg = models.TextField("Message")
    cont_dat = models.DateTimeField("Date d'envoi" ,auto_now=True)
    class Meta:
        db_table= "Contacts"
    def __str__(self):
        return "{0}  |  {1}  |  {2}".format(self.cont_nom, self.cont_mail, self.cont_dat)

class Abonnes(models.Model):
    Abn_mail = models.EmailField("Email")
    Abn_dat = models.DateTimeField("Date d'envoi", auto_now=True)
    class Meta:
        db_table= "Abonnés"
    def __str__(self):
        return "{0}  |  {1}".format(self.Abn_mail, self.Abn_dat)