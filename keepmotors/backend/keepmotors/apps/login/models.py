from django.db import models

# Create your models here.
class login (models.Model):
    correo= models.TextField(("tipo_vehiuculo"))
    contraseña= models.TextField(("placa_vehiculo"))
    
    
   