from rest_framework import serializers
from .models import Alquiler, Pago, Calificacion

class AlquilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alquiler
        fields = ("id","articulo","arrendatario","propietario","fecha_inicio","fecha_fin","estado","precio_total","creado")
        read_only_fields = ("arrendatario","propietario","precio_total")

    def create(self, validated_data):
        request = self.context["request"]
        validated_data["arrendatario"] = request.user
        obj = Alquiler(**validated_data)
        obj.full_clean()
        obj.save()
        return obj

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ("id","alquiler","monto","metodo","estado","fecha")
        read_only_fields = ("estado","fecha")

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = ("id","alquiler","autor","destinatario","puntaje","comentario","fecha")
        read_only_fields = ("autor","fecha")

    def create(self, validated_data):
        validated_data["autor"] = self.context["request"].user
        cal = Calificacion(**validated_data)
        cal.full_clean()
        cal.save()
        return cal
