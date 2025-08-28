from django.db import models
from rest_framework import viewsets, permissions
from .models import Alquiler, Pago, Calificacion
from .serializers import AlquilerSerializer, PagoSerializer, CalificacionSerializer

class AlquilerViewSet(viewsets.ModelViewSet):
    serializer_class = AlquilerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        u = self.request.user
        return Alquiler.objects.filter(models.Q(arrendatario=u) | models.Q(propietario=u)).select_related("articulo")

class PagoViewSet(viewsets.ModelViewSet):
    serializer_class = PagoSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Pago.objects.filter(alquiler__arrendatario=self.request.user)

class CalificacionViewSet(viewsets.ModelViewSet):
    serializer_class = CalificacionSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        u = self.request.user
        return Calificacion.objects.filter(models.Q(autor=u) | models.Q(destinatario=u))
