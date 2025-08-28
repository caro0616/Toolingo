from django.db import models

class TipoUsuario(models.TextChoices):
    PROPIETARIO = 'PROPIETARIO', 'Propietario'
    ARRENDATARIO = 'ARRENDATARIO', 'Arrendatario'
    AMBOS = 'AMBOS', 'Ambos'

class EstadoArticulo(models.TextChoices):
    NUEVO = 'NUEVO', 'Nuevo'
    USADO = 'USADO', 'Usado'
    MUY_USADO = 'MUY_USADO', 'Muy Usado'

class EstadoAlquiler(models.TextChoices):
    SOLICITADO = 'SOLICITADO', 'Solicitado'
    APROBADO = 'APROBADO', 'Aprobado'
    EN_CURSO = 'EN_CURSO', 'En curso'
    FINALIZADO = 'FINALIZADO', 'Finalizado'
    CANCELADO = 'CANCELADO', 'Cancelado'

class MetodoPago(models.TextChoices):
    TARJETA = 'TARJETA', 'Tarjeta'
    NEQUI = 'NEQUI', 'Nequi'
    BANCOLOMBIA = 'BANCOLOMBIA', 'Bancolombia'
    EFECTIVO = 'EFECTIVO', 'Efectivo'

class EstadoPago(models.TextChoices):
    PENDIENTE = 'PENDIENTE', 'Pendiente'
    PAGADO = 'PAGADO', 'Pagado'
    FALLIDO = 'FALLIDO', 'Fallido'

