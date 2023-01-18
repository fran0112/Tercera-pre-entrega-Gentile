from django.urls import path

from blogs.views import saludar, lista_blogs, lista_temas


urlpatterns = [
    path('saludar/', saludar),
    path('lista', lista_blogs),
    path('lista-temas', lista_temas)
    
]