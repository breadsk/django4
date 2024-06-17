from django.db import models

from alumnos.models import Genero
# Create your models here.
class Docente(models.Model):
    rut = models.CharField(primary_key=True,max_length=10)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(blank=False,null=False)
    id_genero = models.ForeignKey('alumnos.Genero',on_delete=models.CASCADE,db_column='idGenero')
    telefono = models.CharField(max_length=45)
    email = models.CharField(unique=True,max_length=100,blank=True,null=True)
    activo = models.IntegerField()

    def __str__(self):
        return str(self.nombre) + " " + str(self.apellido_paterno)
    
    class Meta:
        ordering=['rut']