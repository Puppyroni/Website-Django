from django.shortcuts import render
from galeria.models import Image

def index(request):
    
    set_image = Image.objects.all()
    
    return render(request, 'index.html', {'cards': set_image})

def imagem_page(request):
    return render(request, 'imagem.html')