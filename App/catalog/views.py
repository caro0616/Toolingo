from rest_framework import viewsets, permissions
from .models import Categoria, Articulo
from .serializers import CategoriaSerializer, ArticuloSerializer
from .filters import ArticuloFilter

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.AllowAny]

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.select_related("categoria","propietario").all()
    serializer_class = ArticuloSerializer
    filterset_class = ArticuloFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(propietario=self.request.user)
