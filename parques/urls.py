from django.urls import path
from . import views

app_name = "parques"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("parques/", views.lista_parques, name="lista_parques"),
    path("parques/<int:parque_id>/", views.detalle_parque, name="detalle_parque"),
    path("actividades/", views.actividades, name="actividades"),
    path("contacto/", views.contacto, name="contacto"),
]