
from django.urls import path
from . import views

urlpatterns = [
    path('docentes', views.docentes, name="docentes")
]
