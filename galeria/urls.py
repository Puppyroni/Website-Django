from django.urls import path 
from galeria.views import index, imagem_page

urlpatterns = [path('', index, name='index'),
               path('imagem/', imagem_page, name='imagem')]