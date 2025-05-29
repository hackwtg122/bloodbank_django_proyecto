from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Donante, UnidadSangre, Solicitud

class BaseFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method="post"
        self.add_input(Submit("submit","Guardar"))

class DonanteForm(forms.ModelForm):
    class Meta:
        model = Donante
        fields = ["nombre","edad","tipo_sangre","ultima_donacion","direccion","telefono","historial_medico"]
    def __init__(self,*a,**kw):
        super().__init__(*a,**kw); self.helper=BaseFormHelper()

class UnidadSangreForm(forms.ModelForm):
    class Meta:
        model = UnidadSangre
        fields = ["tipo_sangre","cantidad_ml","fecha_donacion","donante"]
    def __init__(self,*a,**kw):
        super().__init__(*a,**kw); self.helper=BaseFormHelper()

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ["tipo_sangre","cantidad_ml","urgencia","estado"]
    def __init__(self,*a,**kw):
        super().__init__(*a,**kw); self.helper=BaseFormHelper()

from .models import DonantePerfil

class DonantePerfilForm(forms.ModelForm):
    class Meta:
        model = DonantePerfil
        fields = ["tipo_sangre", "edad", "ultima_donacion", "direccion", "telefono", "historial_medico"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = BaseFormHelper()
