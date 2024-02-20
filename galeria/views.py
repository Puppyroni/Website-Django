from django.shortcuts import render

def index(request):
    return render(request, 'index.html') 

def imagem_page(request):
    return render(request, 'imagem.html') 