from django.db import models

# Create your models here.

class pant(models.Model):
    modelo = models.CharField(max_length=60)
    talle = models.CharField(max_length=60)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Modelo: {self.modelo}"    
    def __str__(self):
        return f"Talle y medidas: {self.talle}"
    def __str__(self):
        return f"Modelo: {self.modelo}"
    #modelo_pant = models.CharField(max_length=60)
    #TALLES_CHOICES = ('XL', '40-42'), ('L', '36-38'), ('M', '32-34'), ('S', '28-30')
    #talles = models.CharField(max_length=60, choices=TALLES_CHOICES, default='talles')
    
class shirt(models.Model):
    modelo = models.CharField(max_length=60)
    talle = models.CharField(max_length=60)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Modelo: {self.modelo}"    
    def __str__(self):
        return f"Talle y medidas: {self.talle}"
    def __str__(self):
        return f"Precio: {self.precio}"
    #modelo_shirt = models.CharField(max_length=60)
    #TALLES_CHOICES = ('XL', '40-42'), ('L', '36-38'), ('M', '32-34'), ('S', '28-30')
    #talles = models.CharField(max_length=60, choices=TALLES_CHOICES, default='talles')
class buzo(models.Model):
    modelo = models.CharField(max_length=60)
    talle = models.CharField(max_length=60)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Modelo: {self.modelo}"    
    def __str__(self):
        return f"Talle y medidas: {self.talle}"
    def __str__(self):
        return f"Precio: {self.precio}"
    #modelo_buzo = models.CharField(max_length=60)
    #TALLES_CHOICES = ('XL', '40-42'), ('L', '36-38'), ('M', '32-34'), ('S', '28-30')
    #talles = models.CharField(max_length=60, choices=TALLES_CHOICES, default='talles')
    #modelo_buzo = models.CharField(max_length=60)