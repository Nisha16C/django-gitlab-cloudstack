from django.db import models

# Create your models here.
class SOC(models.Model):
    SIEMxdr = models.BooleanField(default=False)
    monitoring = models.BooleanField(default=False)
    logging = models.BooleanField(default=False)

    