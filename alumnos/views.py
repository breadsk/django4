from django.shortcuts import render
from .models import Genero , Alumno

from .forms import GeneroForm

# Create your views here.
def index(request):    
    context = {}
    return render(request,"alumnos/index.html",context)

def crud(request):
    alumnos = Alumno.objects.all()    
    #alumnos = Alumno.objects.raw("SELECT * from alumnos_alumno")
    context = {"alumnos":alumnos}
    return render(request,"alumnos/alumnos_list.html",context)

def alumnosAdd(request):
    if request.method != "POST":
        #No es un post, por lo tanto se muestra el formulario para agregar
        generos = Genero.objects.all()
        context = { "generos" : generos }
        return render(request,"alumnos/alumnos_add.html", context)
    else:
        generos = Genero.objects.all()
        #Es un post , por ende se recuperan los datos DEL FORMULARIO y 
        #se graban en la tabla
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        objGenero = Genero.objects.get(id_genero = genero)
        obj = Alumno.objects.create(
            rut = rut,
            nombre = nombre,
            apellido_paterno = aPaterno,
            apellido_materno = aMaterno,
            fecha_nacimiento = fechaNac,
            id_genero = objGenero,
            telefono = telefono,
            email = email,
            direccion = direccion,
            activo=1
        )
        obj.save()
        context = { "mensaje": "Alumno guardado satisfactoriamente", "generos":generos }
        return render(request,"alumnos/alumnos_add.html",context)


def alumnos_del(request,pk):
    context= {}
    try:
        alumno = Alumno.objects.get(rut=pk)
        alumno.delete()

        mensaje = "Alumno eliminado satisfactoriamente"
        alumnos = Alumno.objects.all()
        context = {"alumnos":alumnos,"mensaje":mensaje}
        return render(request,"alumnos/alumnos_list.html",context)
    except:
        mensaje = "Error al eliminar"
        alumnos = Alumno.objects.all()
        context = {"alumnos":alumnos,"mensaje":mensaje}
        return render(request,"alumnos/alumnos_list.html",context)

def alumnos_findEdit(request,pk):
    
    if pk != "":
        alumno = Alumno.objects.get(rut=pk)
        generos = Genero.objects.all()

        context = {"alumno":alumno,"generos":generos}

        if alumno:
            return render(request,"alumnos/alumnos_edit.html",context)
        else:
            context = {"mensaje":"Error , el rut no existe"}
            return render(request,"alumnos/alumnos_edit.html",context)


def alumnosUpdate(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]

        objGenero = Genero.objects.get(id_genero = genero)

        alumno = Alumno()
        alumno.rut = rut
        alumno.nombre = nombre
        alumno.apellido_paterno = aPaterno
        alumno.apellido_materno = aMaterno
        alumno.fecha_nacimiento = fechaNac
        alumno.id_genero = objGenero
        alumno.telefono = telefono
        alumno.email = email
        alumno.direccion = direccion
        alumno.activo = 1

        alumno.save()

        generos = Genero.objects.all()
        context = {"mensaje":"Datos actualizados satisfactoriamente","generos":generos,"alumno":alumno}
        return render(request,"alumnos/alumnos_edit.html",context)
    else:
        #No es un post, entoncres se muestra un formulario para acer un add(insert)
        alumnos = Alumno.objects.all
        context = {"alumnos":alumnos}
        return render(request,"alumnos/alumnos_list.html",context)
    
def crud_generos(request):
    generos = Genero.objects.all()
    context = {"generos":generos}
    return render(request,"generos/generos_list.html",context)

def generosAdd(request):
    context= {}
    if request.method == "POST":
        form = GeneroForm(request.POST)
        if form.is_valid:
            form.save()

            #Limpiar mi form
            form = GeneroForm()

            context = {"mensaje":"Genero guardado satisfactoriamente","form":form}
            return render(request,"generos/generos_add.html",context)
    else:
        form = GeneroForm()
        context = {"form":form}
        return render(request,"generos/generos_add.html",context)


def generos_del(request,pk):
    mensajes = []
    errores = []
    generos = Genero.objects.all()
    try:
        genero = Genero.objects.get(id_genero = pk)
        if genero:
            genero.delete()
            mensajes.append("Bien genero eliminado correctamente")
            context = {"generos":generos,"mensajes":mensajes}
            return render(request,"generos/generos_list.html",context)
    except:
        genero = Genero.objects.all()
        mensaje = "Error , el id no existe para ser eliminado"
        context = {"mensaje":mensaje,"generos":generos}
        return render(request,"generos/generos_list.html",context)

def generos_edit(request,pk):
    try:
        genero = Genero.objects.get(id_genero = pk)
        context = {}
        if genero:
            if request.method == "POST":
                form = GeneroForm(request.POST, instance=genero)
                form.save()
                mensaje = "Genero Actualizado Correctamente"
                context = {"genero": genero , "form":form , "mensaje":mensaje}
                return render(request,"generos/generos_edit.html",context)
            else:
                form = GeneroForm(instance=genero)
                mensaje=""
                context = {"genero":genero, "form":form, "mensaje":mensaje}
                return render(request,"generos/generos_edit.html",context)
    except:
        generos = Genero.objects.all()
        mensajes = "Error, el id no existe"
        context = {"mensaje":mensajes, "generos":generos}
        return render(request,"generos/generos_list.html",context)