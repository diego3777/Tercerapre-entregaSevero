from django.db import models 
from django.contrib.auth.models import User
from django.db import models


class equipo (models.Model):
    nombre = models.CharField(max_length=100)
    divisional = models.CharField(max_length=100)
    def  __str__(self):
        return f"{self.nombre} - {self.divisional}"
class jugador (models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    equipo_actual = models.CharField(max_length=100)
    def  __str__(self):
        return f"{self.nombre} - {self.edad} - {self.equipo_actual}"
    
    


class liga(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre}"

from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    contenido_html = models.TextField() 
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    datos_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='post_images/', blank=True, null=True)

    class Meta:
        app_label = 'AppProyecto'  

    def __str__(self):
        return self.titulo
    
    



#class UserProfile(models.Model):
 #   usuario = models.OneToOneField(User, on_delete=models.CASCADE)
  #  nombre = models.CharField(max_length=50)
   # apellido = models.CharField(max_length=50)
    #fecha_nacimiento = models.DateField()  
    #email = models.EmailField()
   
    #def __str__(self):
     #   return self.usuario.username