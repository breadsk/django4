from django.shortcuts import render
from alumnos.models import Alumno
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def menu(request):
    request.session["usuario"] = "cgarcia"
    usuario = request.session["usuario"]
    context = {"usuario":usuario}
    return render(request,"administrador/menu.html",context)

def reporte_alumnos(request):
    alumnos = Alumno.objects.all()
    context = {"alumnos":alumnos}
    return render(request,"administrador/menu.html",context)

def home(request):
    context={}
    return render(request,"administrador/home.html",context)