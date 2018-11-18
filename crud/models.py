from django.db import models

# Create your models here.

class Member(models.Model):
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    DNI = models.CharField(max_length=40)
    Fechanac = models.DateField(blank = True , null = True) 
    def __str__(self):
        return self.Nombre + " " + self.Apellido + " " + self.DNI + " " + Fechanac
