from rest_framework import serializers
from .models import Categoria, Articulo, Imagen

class CategoriaSerializer(serializers.ModelSerializer):
    hijas = serializers.SerializerMethodField()
    class Meta:
        model = Categoria
        fields = ("id","nombre","slug","parent","hijas")
    def get_hijas(self, obj):
        return CategoriaSerializer(obj.hijas.all(), many=True).data

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = ("id","imagen","descripcion")

class ArticuloSerializer(serializers.ModelSerializer):
    imagenes = ImagenSerializer(many=True, required=False)
    class Meta:
        model = Articulo
        fields = ("id","propietario","titulo","descripcion","categoria","estado",
                  "precio_por_dia","deposito","disponibilidad_global","ubicacion","creado","imagenes")
        read_only_fields = ("propietario",)

    def create(self, validated_data):
        imgs = validated_data.pop("imagenes", [])
        articulo = Articulo.objects.create(**validated_data)
        for img in imgs:
            Imagen.objects.create(articulo=articulo, **img)
        return articulo
