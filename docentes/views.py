from django.shortcuts import render
from .models import Docente

# Create your views here.
def docentes(request):
    docentes = Docente.objects.all()
    context= {"docentes":docentes}
    return render(request,"docentes/docentes.html",context)
