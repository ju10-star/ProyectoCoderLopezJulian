from django.db import models

# Create your models here.

class pant(models.Model):
    modelo_pant = models.CharField(max_length=60)
    talles = {"XL" : "40-42",
             "L"  : "36-38",
             "M"  : "32-34",
             "S"  : "28-30"}
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Modelo: {self.modelo_pant}"    
    def __str__(self):
        return f"Talle y medidas: {self.talles}"
    def __str__(self):
        return f"Modelo: {self.modelo_pant}"
    
class shirt(models.Model):
    modelo_shirt = models.CharField(max_length=60)
    talles = {"XL" : "40-42",
             "L"  : "36-38",
             "M"  : "32-34",
             "S"  : "28-30"}
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Modelo: {self.modelo_shirt}"    
    def __str__(self):
        return f"Talle y medidas: {self.talles}"
    def __str__(self):
        return f"Precio: {self.precio}"
class buzo(models.Model):
    modelo_buzo = models.CharField(max_length=60)
    talles = {"XL" : "40-42",
             "L"  : "36-38",
             "M"  : "32-34",
             "S"  : "28-30"}
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Modelo: {self.modelo_buzo}"    
    def __str__(self):
        return f"Talle y medidas: {self.talles}"
    def __str__(self):
        return f"Precio: {self.precio}"