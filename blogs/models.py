from django.db import models

class Blog(models.Model):
    titulo= models.CharField(max_length=64)
    posteo= models.TextField()
    fecha_posteo= models.DateTimeField()

def __str__(self):  
    return f"{self.titulo}, {self.fecha_posteo}"


class Bloguer(models.Model):
    nombre= models.CharField(max_length=128)
    apellido= models.CharField(max_length=128)
    nombre_usuario= models.CharField(max_length=128)
    email= models.EmailField()
    hobbies= models.CharField(max_length=256)
    bio= models.TextField()


def __str__(self): 
    return f"{self.nombre_usuario}, {self.nombre}"


class Tema(models.Model):
    nombre= models.CharField(max_length=20)

def __str__(self): 
    return f"{self.nombre}"

