from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

TIPOS = [
    ("O+", "O+"), ("O-", "O-"),
    ("A+", "A+"), ("A-", "A-"),
    ("B+", "B+"), ("B-", "B-"),
    ("AB+", "AB+"), ("AB-", "AB-")
]

class Donante(models.Model):
    nombre = models.CharField(max_length=120)
    edad = models.PositiveIntegerField(null=True, blank=True)
    tipo_sangre = models.CharField(max_length=3, choices=TIPOS)
    ultima_donacion = models.DateField(null=True, blank=True)
    direccion = models.TextField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    historial_medico = models.TextField(blank=True)
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("donante_detail", args=[self.id])

class UnidadSangre(models.Model):
    tipo_sangre = models.CharField(max_length=3, choices=TIPOS)
    cantidad_ml = models.PositiveIntegerField()
    fecha_donacion = models.DateField()
    donante = models.ForeignKey(Donante, related_name="unidades", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.tipo_sangre} - {self.cantidad_ml} ml"

class Solicitud(models.Model):
    URGENCIAS = [
        ("baja", "Baja"),
        ("media", "Media"),
        ("alta", "Alta")
    ]
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("aprobada", "Aprobada"),
        ("rechazada", "Rechazada")
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # <-- CAMPO NECESARIO
    tipo_sangre = models.CharField(max_length=3, choices=TIPOS)
    cantidad_ml = models.PositiveIntegerField()
    urgencia = models.CharField(max_length=10, choices=URGENCIAS, default="media")
    estado = models.CharField(max_length=10, choices=ESTADOS, default="pendiente")
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo_sangre} {self.cantidad_ml}ml"

class DonantePerfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_sangre = models.CharField(max_length=3, choices=TIPOS)
    edad = models.PositiveIntegerField(null=True, blank=True)
    ultima_donacion = models.DateField(null=True, blank=True)
    direccion = models.TextField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    historial_medico = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def crear_perfil_donante(sender, instance, created, **kwargs):
    if created:
        DonantePerfil.objects.create(user=instance)
