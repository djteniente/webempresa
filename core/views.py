from django.shortcuts import render, HttpResponse

# Create your views here.


"""
Inicio home/
Historio about
Servicios services/
Visitanos store/
Contacto contact/
Blog blog/
Sample sample/
"""

def home(request):
    return HttpResponse("Inicio")