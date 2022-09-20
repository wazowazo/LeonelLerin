from pydoc import doc
from django.http import HttpResponse
from django.shortcuts import render
from AppLerin.models import Padre
from django.template import loader


def papa(self):
    papa1 = Padre(nombre='Cacho', edad='37',profesion='Panadero')
    papa1.save()
    resultado = f"Mi padre se llama {papa1.nombre},su edad es {papa1.edad}, y su trabajo es {papa1.profesion}"
    return HttpResponse(resultado)