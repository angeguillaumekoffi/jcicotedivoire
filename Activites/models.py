from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Statut_Activite(models.Model):
    statut = models.CharField(max_length=15, primary_key=True, verbose_name="Statut")
    def __str__(self):
        return self.statut



class Activites(models.Model):
    statut_actv = models.ForeignKey(Statut_Activite, on_delete=models.CASCADE, verbose_name="Statut")
    titre = models.CharField("Titre", max_length=100, null=True,)
    date_pub = models.DateTimeField(auto_now= True, verbose_name="Date de publication")
    contenu_actv = RichTextField(null=True, verbose_name="Contenu")
    img = models.ImageField("Image", null=True, upload_to='images/')

    def __str__(self):
        return '%s : %s' %(self.titre, self.date_pub)

    class Meta:
        db_table = "Activites"

class BandeInfo(models.Model):
    dat_pub = models.DateTimeField("Date de publication", auto_now=True)
    info = models.CharField("Info" ,null=True, max_length=200)
    def __str__(self):
        return '{0} | {1} | {2}'.format(self.id, self.dat_pub, self.info)
    class Meta:
        db_table = "Bande d'info"