from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import *

def saludar(request):
    return HttpResponse('Hola esta es mi primer pagina WEB!!!')

def lista_blogs(request):
    contexto= {
        'blogs': Blog.objects.all()
    }
    return render(request=request, 
    template_name='blogs/lista_blogs.html',
    context= contexto
    )

def lista_temas(request):
    return render(request=request, template_name='blogs/lista_temas.html')