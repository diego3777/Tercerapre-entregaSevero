from django import forms
from .models import equipo, jugador, liga

class EquipoForm(forms.ModelForm):
    class Meta:
        model = equipo
        fields = ['nombre', 'divisional']

class JugadorForm(forms.ModelForm):
    class Meta:
        model = jugador
        fields = ['nombre', 'edad', 'equipo']

class LigaForm(forms.ModelForm):
    class Meta:
        model = liga
        fields = ['nombre']
