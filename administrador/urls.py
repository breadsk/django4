from django.urls import path
from . import views

urlpatterns = [ 
    path('menu' , views.menu , name="menu" ),
    path('reporte_alumnos', views.reporte_alumnos,name="reporte_alumnos"),
    path('home',views.home,name="home")
]