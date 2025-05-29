from django.contrib import admin
from .models import Donante, UnidadSangre, Solicitud, DonantePerfil

@admin.register(Donante)
class DonanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_sangre', 'ultima_donacion')
    search_fields = ('nombre', 'tipo_sangre')
    list_filter = ('tipo_sangre',)

@admin.register(UnidadSangre)
class UnidadSangreAdmin(admin.ModelAdmin):
    list_display = ('tipo_sangre', 'cantidad_ml', 'fecha_donacion', 'donante')
    list_filter = ('tipo_sangre', 'fecha_donacion')
    search_fields = ('donante__nombre',)

@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo_sangre', 'cantidad_ml', 'urgencia', 'estado', 'fecha')
    list_filter = ('tipo_sangre', 'urgencia', 'estado', 'fecha')
    search_fields = ('usuario__username',)

@admin.register(DonantePerfil)
class DonantePerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'tipo_sangre', 'ultima_donacion')
    list_filter = ('tipo_sangre',)
