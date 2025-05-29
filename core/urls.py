from django.contrib.auth import views as auth_views
from django.urls import path
from core.views import DonanteDetailView
from .views import perfil_usuario
from .views import (
    UnidadCreateView, SolicitudCreateView,
    UnidadListView, SolicitudListView, DonanteListView,
    UnidadUpdateView, SolicitudUpdateView,
    UnidadDeleteView, SolicitudDeleteView,
    DonanteCreateView, DonanteUpdateView, DonanteDeleteView,
    inicio, reportes_view, buscar_donantes
)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', inicio, name='inicio'),

    # Perfil
    path('perfil/', login_required(perfil_usuario), name='perfil'),

    # Donantes
    path('donantes/', login_required(DonanteListView.as_view()), name='donantes'),
    path('donantes/nuevo/', login_required(DonanteCreateView.as_view()), name='donante-crear'),
    path('donantes/<int:pk>/editar/', login_required(DonanteUpdateView.as_view()), name='donante-editar'),
    path('donantes/<int:pk>/eliminar/', login_required(DonanteDeleteView.as_view()), name='donante-eliminar'),
    path('donantes/<int:pk>/', login_required(DonanteDetailView.as_view()), name='donante_detail'),
    path('donantes/buscar/', login_required(buscar_donantes), name='buscar-donantes'),

    # Unidades
    path('unidades/', login_required(UnidadListView.as_view()), name='unidades'),
    path('unidades/nueva/', login_required(UnidadCreateView.as_view()), name='crear-unidad'),
    path('unidades/<int:pk>/editar/', login_required(UnidadUpdateView.as_view()), name='unidad-editar'),
    path('unidades/<int:pk>/eliminar/', login_required(UnidadDeleteView.as_view()), name='unidad-eliminar'),

    # Solicitudes
    path('solicitudes/', login_required(SolicitudListView.as_view()), name='solicitudes'),
    path('solicitudes/nueva/', login_required(SolicitudCreateView.as_view()), name='crear-solicitud'),
    path('solicitudes/<int:pk>/editar/', login_required(SolicitudUpdateView.as_view()), name='solicitud-editar'),
    path('solicitudes/<int:pk>/eliminar/', login_required(SolicitudDeleteView.as_view()), name='solicitud-eliminar'),

    # Reportes
    path('reportes/', login_required(reportes_view), name='reportes'),

    # Auth
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
]