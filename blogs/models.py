from django.db import models

class Blog(models.Model):
    titulo= models.CharField(max_length=64)
    posteo= models.TextField()
    fecha_posteo= models.DateTimeField()


class Bloguer(models.Model):
    nombre= models.CharField(max_length=128)
    apellido= models.CharField(max_length=128)
    nombre_usuario= models.CharField(max_length=128)
    email= models.EmailField()
    hobbies= models.CharField(max_length=256)
    bio= models.TextField()


class Tema(models.Model):
    nombre= models.CharField(max_length=20)

