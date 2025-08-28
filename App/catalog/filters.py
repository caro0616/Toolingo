import django_filters as df
from .models import Articulo

class ArticuloFilter(df.FilterSet):
    precio_min = df.NumberFilter(field_name="precio_por_dia", lookup_expr="gte")
    precio_max = df.NumberFilter(field_name="precio_por_dia", lookup_expr="lte")
    categoria = df.CharFilter(field_name="categoria__slug", lookup_expr="iexact")
    ubicacion = df.CharFilter(field_name="ubicacion", lookup_expr="icontains")

    class Meta:
        model = Articulo
        fields = ["estado"]
