from django import forms
from .models import equipo, jugador, liga
from .models import Post  
from django.forms import ImageField

class EquipoForm(forms.ModelForm):
    class Meta:
        model = equipo
        fields = ['nombre', 'divisional']

class JugadorForm(forms.ModelForm):
    class Meta:
        model = jugador
        fields = ['nombre', 'edad', 'equipo_actual']


class LigaForm(forms.ModelForm):
    class Meta:
        model = liga
        fields = ['nombre']
        
        
class BusquedaJugadorForm(forms.Form):
    nombre_jugador = forms.CharField(label='Nombre del jugador', max_length=100)
    
    
class PostForm(forms.ModelForm):
    imagen = ImageField(required=False)  

    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'imagen']