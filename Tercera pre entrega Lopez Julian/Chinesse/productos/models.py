from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class pant(models.Model):
    modelo = models.CharField(max_length=60)
    talle = models.CharField(max_length=60)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Modelo: {self.modelo}    ,      Talle: {self.talle}    ,      Precio: {self.precio}" 
    #TALLES_CHOICES = ('XL', '40-42'), ('L', '36-38'), ('M', '32-34'), ('S', '28-30')
    #talles = models.CharField(max_length=60, choices=TALLES_CHOICES, default='talles')
    
class shirt(models.Model):
    modelo = models.CharField(max_length=60)
    talle = models.CharField(max_length=60)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Modelo: {self.modelo}    ,      Talle: {self.talle}    ,      Precio: {self.precio}"
    #TALLES_CHOICES = ('XL', '40-42'), ('L', '36-38'), ('M', '32-34'), ('S', '28-30')
    #talles = models.CharField(max_length=60, choices=TALLES_CHOICES, default='talles')

class buzo(models.Model):
    modelo = models.CharField(max_length=60)
    talle = models.CharField(max_length=60)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Modelo: {self.modelo}    ,      Talle: {self.talle}       ,   Precio: {self.precio}"
    #TALLES_CHOICES = ('XL', '40-42'), ('L', '36-38'), ('M', '32-34'), ('S', '28-30')
    #talles = models.CharField(max_length=60, choices=TALLES_CHOICES, default='talles')
    
class avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user} {self.imagen}"