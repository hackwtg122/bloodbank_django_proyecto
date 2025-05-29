from django.contrib.auth.models import User
from core.models import DonantePerfil, Solicitud, UnidadSangre
from django.utils import timezone
from random import choice, randint
import datetime

TIPOS = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
nombres = ["jairo", "ana", "carlos", "lucia", "valeria", "daniel", "sofia", "pablo", "mario", "ines"]

User.objects.exclude(is_superuser=True).delete()
DonantePerfil.objects.all().delete()
Solicitud.objects.all().delete()
UnidadSangre.objects.all().delete()

for nombre in nombres:
    u = User.objects.create_user(username=nombre, password="12345")
    d = u.donanteperfil
    d.tipo_sangre = choice(TIPOS)
    d.edad = randint(18, 65)
    d.ultima_donacion = timezone.now().date() - datetime.timedelta(days=randint(30, 300))
    d.direccion = f"Calle {randint(1,100)}"
    d.telefono = f"300{randint(1000000,9999999)}"
    d.historial_medico = "Sin antecedentes"
    d.save()
    for _ in range(randint(1, 3)):
        UnidadSangre.objects.create(
            tipo_sangre=d.tipo_sangre,
            cantidad_ml=randint(250, 500),
            fecha_donacion=timezone.now().date() - datetime.timedelta(days=randint(1, 100)),
            donante=None
        )

for _ in range(6):
    Solicitud.objects.create(
        tipo_sangre=choice(TIPOS),
        cantidad_ml=randint(300, 600),
        urgencia=choice(["baja", "media", "alta"]),
        estado="pendiente"
    )

print("✔ Usuarios, perfiles, unidades y solicitudes cargados.")