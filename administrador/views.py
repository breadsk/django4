from django.shortcuts import render
from alumnos.models import Alumno

# Create your views here.
def menu(request):
    context = {}
    return render(request,"administrador/menu.html",context)
def reporte_alumnos(request):
    alumnos = Alumno.objects.all()
    context = {"alumnos":alumnos}
    return render(request,"administrador/menu.html",context)