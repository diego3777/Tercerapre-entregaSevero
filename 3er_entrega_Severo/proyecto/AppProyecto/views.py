from django.shortcuts import render
from django.http import HttpResponse
from .models import equipo, jugador, liga

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

def formulario_equipo(request):
    return render(request, "AppTemplates/formulario_equipo.html")


def formulario_ligas(request):
    ligas = liga.objects.all()  
    return render(request, "AppTemplates/formulario_liga.html", {"ligas": ligas})


def formulario_jugadores(request):
    jugadores = jugador.objects.all()  
    return render(request, "AppTemplates/formulario_jugador.html", {"jugadores": jugadores})

    