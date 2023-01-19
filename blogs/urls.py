from django.urls import path

from blogs.views import lista_blogs, lista_temas, lista_bloguers


urlpatterns = [
    path('blogs', lista_blogs, name="listar_blogs"),
    path('temas', lista_temas, name= "listar_temas"),
    path('bloguers', lista_bloguers, name= "listar_bloguers"),
    
]