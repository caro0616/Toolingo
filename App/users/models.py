from django.db import models

# Create your models here.
import uuid
from django.contrib.auth.models import AbstractUser
from common.enums import TipoUsuario

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=120, blank=True)
    direccion = models.CharField(max_length=250, blank=True)
    telefono = models.CharField(max_length=30, blank=True)
    tipo_usuario = models.CharField(max_length=20, choices=TipoUsuario.choices, default=TipoUsuario.AMBOS)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # para admin

    def __str__(self):
        return self.email
