from django.db import models

# Create your models here.
class Cuenta(models.Model):
    name = models.CharField(max_length=15)
    saldo = models.FloatField()
    def __str__(self):
        return self.name
