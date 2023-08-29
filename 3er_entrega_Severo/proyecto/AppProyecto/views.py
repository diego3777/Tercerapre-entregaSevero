from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import equipo, jugador, liga
from .forms import LigaForm, EquipoForm, JugadorForm

def ingresar_equipo(request):
    nombre_equipo = "Nacional"
    divisional = "A"
    print("ingresando equipo")
    nuevo_equipo = equipo(nombre=nombre_equipo, divisional=divisional)
    nuevo_equipo.save()
    respuesta = f"Equipo ingresado: {nuevo_equipo.nombre} - {nuevo_equipo.divisional}"
    return HttpResponse(respuesta)

def lista_equipos(request):
    equipos = equipo.objects.all()
    respuesta = ""
    for un_equipo in equipos:
        respuesta += f"{un_equipo.nombre} - {un_equipo.divisional}"

    return HttpResponse(respuesta)

def inicio(request):
    return render(request, "AppTemplates/inicio.html")

def todos_equipos(request):
    equipos = equipo.objects.all()  
    return render(request, "AppTemplates/equipo.html", {"equipos": equipos})

    

def equipos(request):
    equipos = equipo.objects.all()
    return render(request, "AppTemplates/equipo.html", {"equipos": equipos})

def ver_jugadores(request):
    jugadores = jugador.objects.all()  
    return render(request, "AppTemplates/jugador.html", {"jugadores": jugadores})

def ver_ligas(request):
    ligas_lista = liga.objects.all()  
    return render(request, "AppTemplates/liga.html", {"ligas": ligas_lista})

#FORMULARIOS

def formulario_jugadores(request):
    if request.method == "POST":
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "AppTemplates/formulario_jugador.html", {"mensaje": "Jugador creado", "form": form})
        else:
            return render(request, "AppTemplates/formulario_jugador.html", {"mensaje": "Datos inválidos", "form": form})
    else:
        form = JugadorForm()

    return render(request, "AppTemplates/formulario_jugador.html", {"form": form})


def formulario_equipo(request):
    if request.method == "POST":
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "AppTemplates/formulario_equipo.html", {"mensaje": "Equipo creado", "form": form})
        else:
            return render(request, "AppTemplates/formulario_equipo.html", {"mensaje": "Datos inválidos", "form": form})
    else:
        form = EquipoForm()

    return render(request, "AppTemplates/formulario_equipo.html", {"form": form})


def formulario_ligas(request):
    if request.method == "POST":
        form = LigaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "AppTemplates/formulario_liga.html", {"mensaje": "Liga creada", "form": form})
        else:
            return render(request, "AppTemplates/formulario_liga.html", {"mensaje": "Datos inválidos", "form": form})
        
        
    else:
        form = LigaForm()

    return render(request, "AppTemplates/formulario_liga.html", {"form": form})

#BUSQUEDA

from .forms import BusquedaJugadorForm

def resultados_busqueda_jugadores(request):
    form = BusquedaJugadorForm(request.GET)
    jugadores = []

    if form.is_valid():
        nombre_jugador = form.cleaned_data['nombre_jugador']
        jugadores = jugador.objects.filter(nombre__icontains=nombre_jugador)

    return render(request, "AppTemplates/resultados_busqueda_jugadores.html", {"jugadores": jugadores, "form": form})





    