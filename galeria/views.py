from django.shortcuts import render
from galeria.models import Image

def index(request):
    
    set_image = Image.objects.filter(published = True)
    
    return render(request, 'galeria/index.html', {'cards': set_image})

def imagem_page(request):
    return render(request, 'galeria/imagem.html')