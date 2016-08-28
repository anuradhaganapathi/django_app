from django.db import models

# Create your models here.

class sites(models.Model):
    site_name = models.CharField(max_length=10)
    Date = models.DateField()
    Avalue = models.FloatField()
    Bvalue = models.FloatField()
