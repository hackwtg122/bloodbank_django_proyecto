def run():
    from core.models import Donante, UnidadSangre, Solicitud
    from django.contrib.auth.models import User
    from django.utils import timezone
    from random import choice, randint
    import datetime

    TIPOS = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
    nombres = ["Luis", "Ana", "Carlos", "Maria", "Pedro", "Lucia", "Juan", "Valeria", "Sofia", "Miguel"]

    Donante.objects.all().delete()
    UnidadSangre.objects.all().delete()
    Solicitud.objects.all().delete()
    User.objects.exclude(is_superuser=True).delete()

    usuario = User.objects.create_user(username="temporal", password="12345")

    donantes = []
    for nombre in nombres:
        d = Donante.objects.create(
            nombre=nombre,
            edad=randint(18, 60),
            tipo_sangre=choice(TIPOS),
            ultima_donacion=timezone.now().date() - datetime.timedelta(days=randint(30, 365)),
            direccion=f"Calle {randint(1,100)}",
            telefono=f"300{randint(1000000,9999999)}",
            historial_medico="Sin antecedentes"
        )
        donantes.append(d)

    for _ in range(20):
        UnidadSangre.objects.create(
            tipo_sangre=choice(TIPOS),
            cantidad_ml=randint(250, 500),
            fecha_donacion=timezone.now().date() - datetime.timedelta(days=randint(1, 100)),
            donante=choice(donantes)
        )

    for _ in range(5):
        Solicitud.objects.create(
            tipo_sangre=choice(TIPOS),
            cantidad_ml=randint(300, 600),
            urgencia=choice(["baja", "media", "alta"]),
            estado="pendiente",
            usuario=usuario
        )

    print("✔ Datos de prueba insertados correctamente.")