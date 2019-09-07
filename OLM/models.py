from django.db import models

# Create your models here.

class Region(models.Model):
    Nom_Redion = models.CharField("Non de region", primary_key=True, max_length=25)
    vpen = models.CharField("VPEN", max_length=50)

    def __str__(self):
        return self.Nom_Redion

class Zone(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    Nom_Zone = models.CharField("Non de zone", primary_key=True, max_length=25)
    vpn_a = models.CharField("VPN A", max_length=50)

    def __str__(self):
        return self.Nom_Zone

class OLM(models.Model):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    olm = models.CharField("OLM", max_length=50)

    def __str__(self):
        return self.olm

    class Meta:
        db_table = "OLM"