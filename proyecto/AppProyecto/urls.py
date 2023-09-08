from django.urls import path
from .views import *
from . import views
from .forms import PostForm

urlpatterns = [
    path('', inicio, name='inicio'), 
    path("ingresar_equipo/", ingresar_equipo),
    path("listar_equipos/", lista_equipos),
    path("liga/", ver_ligas, name="ligas"),  
    path("jugador/", ver_jugadores, name="jugadores"),
    path("equipos/", equipos, name="equipos"),  
    path("formulario_equipo/", formulario_equipo, name="formulario_equipo"),
    path("formulario_liga/", formulario_ligas, name="formulario_liga"),
    path("formulario_jugador/", formulario_jugadores, name="formulario_jugador"),
    path("resultados_busqueda_jugadores/", resultados_busqueda_jugadores, name="resultados_busqueda_jugadores"),
    path('cargar_post/', views.cargar_post, name='cargar_post'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),

]


