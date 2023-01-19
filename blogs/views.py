from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import *

def inicio(request):
    return render(request=request,
    template_name='blogs/inicio.html',
    )

def lista_blogs(request):
    contexto= {
        'blogs': Blog.objects.all()
    }
    return render(request=request, 
    template_name='blogs/lista_blogs.html',
    context= contexto
    )

def lista_temas(request):
    contexto= {
        'temas': Tema.objects.all()
    }
    return render(request=request,
     template_name='blogs/lista_temas.html',
     context=contexto)


def lista_bloguers(request):
    contexto= {
        'bloguers': Bloguer.objects.all()
    }
    return render(request=request,
     template_name='blogs/lista_bloguers.html',
     context=contexto)