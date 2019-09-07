from django.db import models

# Create your models here.
choix = [
    ("National", "National"),
    ('International', 'international')
]


class Institutions(models.Model):
    institution = models.CharField("Institution", max_length=50)
    respo = models.CharField("Responsable", max_length=50)
    def __str__(self):
        return '{0} : {1}'.format(self.institution, self.respo)
    class Meta:
        db_table="Institutions"

class Plan(models.Model):
    axe = models.TextField("Axe")
    def __str__(self):
        return 'Axe {0} : {1}'.format(self.id, self.axe)
    class Meta:
        db_table="Plan_stratégique"

class DonneesPresi(models.Model):
    ordre = models.CharField("Ordre", max_length=15, choices=choix)
    mdt = models.CharField("Mandat", max_length=10)
    Nom_Pren = models.CharField("Nom et prenoms", max_length=100)
    origin = models.CharField("Origine", max_length=40)
    photo = models.ImageField("Photo", upload_to='Presidents/', blank=True, null=True)
    def __str__(self):
        return '{0} : {1}'.format(self.ordre, self.Nom_Pren)
    class Meta:
        db_table="DonneesPresident"