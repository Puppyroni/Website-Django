from django.shortcuts import render
from utilizadores.forms import LoginForm

def login(request):
    get_form = LoginForm()
    
    return render(request, 'utilizadores/login.html', {'form': get_form})

def regist(request):
    return render(request, 'utilizadores/registo.html')