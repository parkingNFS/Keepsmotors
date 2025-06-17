from rest_framework import serializers
from .models import *


class loginSerializer(serializers.ModelSerializer):
    correo= models.TextField(("tipo_vehiuculo"))
    contraseña= models.TextField(("placa_vehiculo"))