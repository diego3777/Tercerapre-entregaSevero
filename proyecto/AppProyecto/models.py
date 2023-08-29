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
