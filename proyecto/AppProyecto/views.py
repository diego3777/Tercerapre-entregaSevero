from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import equipo, jugador, liga, Post, UserProfile
from .forms import LigaForm, EquipoForm, JugadorForm
from django.shortcuts import get_object_or_404
from .forms import PostForm
from .models import Post
from django.utils.html import escape
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from .forms import UserProfileForm
from django.contrib import messages 



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
 
    posts = Post.objects.all().order_by('-datos_publicacion')[:5] 
    return render(request, '/Users/diego/Desktop/ProyectoDiegoSevero/proyecto/AppProyecto/templates/AppTemplates/inicio.html', {'posts': posts})


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

#Blog

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        contenido = request.POST['contenido']
        autor = request.user
        nueva_publicacion = Post(titulo=titulo, contenido=contenido, autor=autor)
        nueva_publicacion.save()
        return redirect('home')
    return render(request, 'blog/create_post.html')

@login_required(login_url='iniciar_sesion')
def cargar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.contenido_html = escape(post.contenido)
            post.save()
            return redirect('inicio')  
    else:
        form = PostForm()
    return render(request, 'AppTemplates/crear_post_form.html', {'form': form})

def mostrar_posts(request):
    posts = Post.objects.all().order_by('-datos_publicacion')[:5]
    return render(request, 'AppTemplates/inicio.html', {'posts': posts})

from django.shortcuts import render
from .models import Post



#LOGIN

from django.contrib.auth import authenticate, login


def registro_usuario(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.usuario = user
            profile.save()
            login(request, user)
            messages.success(request, "¡Registro exitoso!")  # Mensaje de éxito
            return redirect('inicio') 
        else:
            messages.error(request, "Por favor, corrige los errores en el formulario.")  # Mensaje de error
    else:
        user_form = UserCreationForm()
        profile_form = UserProfileForm()

    return render(
        request,
        'registro_usuario.html',
        {'user_form': user_form, 'profile_form': profile_form}
    )



def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')  
        else:
           
            return render(request, 'login.html', {'error_message': 'Credenciales inválidas'})
    return render(request, 'login.html')

@login_required
def custom_logout(request):
    return LogoutView.as_view()(request)


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm

@login_required
def view_profile(request):
    profile = UserProfile.objects.get(usuario=request.user)
    return render(request, 'ver_perfil.html', {'profile': profile})



    