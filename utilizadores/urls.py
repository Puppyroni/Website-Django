from django.urls import path 
from utilizadores.views import login, regist
    
urlpatterns = [
        path('login', login, name = 'login'),
        path('registo', regist, name = 'registo'),
    ]