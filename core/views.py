from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Donante, UnidadSangre, Solicitud
from .forms import DonanteForm, UnidadSangreForm, SolicitudForm
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def perfil_usuario(request):
    return render(request, 'core/perfil.html')

# Inicio
def inicio(request):
    return render(request, 'core/inicio.html')

class DonanteDetailView(DetailView):
    model = Donante
    template_name = 'core/donante_detail.html'

# Donantes CRUD
class DonanteListView(ListView):
    model = Donante
    template_name = 'core/donante_list.html'
    context_object_name = 'donantes'

    def get_queryset(self):
        qs = super().get_queryset()
        print("⚠️ Donantes cargados:", list(qs))
        return qs

class DonanteCreateView(SuccessMessageMixin, CreateView):
    model = Donante
    form_class = DonanteForm
    template_name = 'core/donante_form.html'
    success_url = reverse_lazy('donantes')
    success_message = "Donante registrado exitosamente."

class DonanteUpdateView(SuccessMessageMixin, UpdateView):
    model = Donante
    form_class = DonanteForm
    template_name = 'core/donante_form.html'
    success_url = reverse_lazy('donantes')
    success_message = "Donante actualizado correctamente."

class DonanteDeleteView(DeleteView):
    model = Donante
    template_name = 'core/donante_confirm_delete.html'
    success_url = reverse_lazy('donantes')

# Unidades CRUD
class UnidadListView(ListView):
    model = UnidadSangre
    template_name = 'core/unidadsangre_list.html'

class UnidadCreateView(SuccessMessageMixin, CreateView):
    model = UnidadSangre
    form_class = UnidadSangreForm
    template_name = 'core/unidad_form.html'
    success_url = reverse_lazy('unidades')
    success_message = "Unidad registrada exitosamente."

class UnidadUpdateView(SuccessMessageMixin, UpdateView):
    model = UnidadSangre
    form_class = UnidadSangreForm
    template_name = 'core/unidad_form.html'
    success_url = reverse_lazy('unidades')
    success_message = "Unidad actualizada correctamente."

class UnidadDeleteView(DeleteView):
    model = UnidadSangre
    template_name = 'core/unidad_confirm_delete.html'
    success_url = reverse_lazy('unidades')

# Solicitudes CRUD
class SolicitudListView(ListView):
    model = Solicitud
    template_name = 'core/solicitud_list.html'
    context_object_name = 'solicitudes'

class SolicitudCreateView(SuccessMessageMixin, CreateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'core/solicitud_form.html'
    success_url = reverse_lazy('solicitudes')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        messages.success(self.request, "Solicitud enviada correctamente.")
        return super().form_valid(form)

class SolicitudUpdateView(SuccessMessageMixin, UpdateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'core/solicitud_form.html'
    success_url = reverse_lazy('solicitudes')
    success_message = "Solicitud actualizada correctamente."

class SolicitudDeleteView(DeleteView):
    model = Solicitud
    template_name = 'core/solicitud_confirm_delete.html'
    success_url = reverse_lazy('solicitudes')

# Reporte
def reportes_view(request):
    inventario = UnidadSangre.objects.all()
    tipos = {}
    for u in inventario:
        if u.tipo_sangre not in tipos:
            tipos[u.tipo_sangre] = {"total": 0, "count": 0}
        tipos[u.tipo_sangre]["total"] += u.cantidad_ml
        tipos[u.tipo_sangre]["count"] += 1
    return render(request, 'core/reportes.html', {'tipos': tipos})

# Búsqueda Donantes
def buscar_donantes(request):
    q = request.GET.get("q")
    resultados = Donante.objects.filter(nombre__icontains=q) if q else []
    return render(request, "core/buscar_donantes.html", {"resultados": resultados, "q": q})