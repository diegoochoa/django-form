from django.contrib import admin
from django.urls import path, include
from forms import views

app_name = 'forms'
urlpatterns = [
    path('', views.index, name='mi_form')
]
