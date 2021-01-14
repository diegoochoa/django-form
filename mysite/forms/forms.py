from django import forms
from forms.models import Usuarios
from datetime import datetime


class RegistrarUsuario(forms.Form):
    nombre = forms.CharField(label='Nombre:', max_length=50,
                             widget=forms.TextInput(
                                 attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Nombre',
                                 }))
    telefono = forms.CharField(label='Teléfono', max_length=12,
                               widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control',
                                         'placeholder': '4421234567',
                                     }))
    fecha_de_nacimiento = forms.DateField(label='Fecha de nacimiento:',
                                          widget=forms.SelectDateWidget(years=range(1900, 2001),
                                                                        attrs={
                                                'class': 'form-control',
                                          }))
    email = forms.EmailField(label='Email:', max_length=254,
                             widget=forms.EmailInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'ejemplo@ejemplo.com',
                                   }))
    direccion = forms.CharField(label='Direccion:', max_length=250,
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Direccion',
                                    }))

    def registrar_usuario(self, arg):
        fecha = datetime(int(self.data['fecha_de_nacimiento_year']),
                         int(self.data['fecha_de_nacimiento_month']),
                         int(self.data['fecha_de_nacimiento_day']))

        nuevo_usuario = Usuarios(nombre=self.data['nombre'],
                                 telefono=self.data['telefono'],
                                 fecha_de_nacimiento=fecha,
                                 email=self.data['email'],
                                 direccion=self.data['direccion'])
        nuevo_usuario.save()
        return nuevo_usuario
