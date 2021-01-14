from django.shortcuts import render, redirect
from .forms import RegistrarUsuario
from django.http import HttpResponse
# Create your views here.


def index(request):
    if request.method == 'POST':
        register_form = RegistrarUsuario(request.POST)
        if register_form.is_valid():
            success = register_form.registrar_usuario(request.user)
            print(success.nombre)
            documento = """<html>
            <body>
               El nombre introducido es: %s <br>
               El telefono introducido es: %s <br>
               La fecha de nacimiento introducida es: %s <br>
               El correo introducido es: %s <br>
               La direccion introducida es: %s <br>
            </body>
            </html> 
            """ % (success.nombre, success.telefono, success.fecha_de_nacimiento, success.email, success.direccion)
            return HttpResponse(documento)
    else:
        register_form = RegistrarUsuario()
        return render(request, 'forms/mi_form.html', {'register_form': register_form})
