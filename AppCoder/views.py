from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.
def inicio(self):
    return HttpResponse('vista inicio')

def cursos(self):
    return HttpResponse('vista cursos')

def profesores(self):
    return HttpResponse('vista profesores')

def entregables(self):
    return HttpResponse('vista entregables')

def estudiantes(self):
    return HttpResponse('vista estudiantes')