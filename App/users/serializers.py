from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","email","nombre","direccion","telefono","tipo_usuario")
