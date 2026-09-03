import json
import os
from django.conf import settings
from django.http import Http404
from django.shortcuts import render


def cargar_parques():
    ruta = os.path.join(settings.BASE_DIR, "parques", "data", "parques.json")
    with open(ruta, encoding="utf-8") as archivo:
        return json.load(archivo)


def inicio(request):
    parques = cargar_parques()
    contexto = {"destacados": parques[:3]}
    return render(request, "parques/inicio.html", contexto)


def lista_parques(request):
    parques = cargar_parques()
    contexto = {"parques": parques}
    return render(request, "parques/parques.html", contexto)


def detalle_parque(request, parque_id):
    parques = cargar_parques()
    parque = next((p for p in parques if p["id"] == parque_id), None)
    if parque is None:
        raise Http404("Parque no encontrado")
    return render(request, "parques/detalle.html", {"parque": parque})


def actividades(request):
    parques = cargar_parques()
    contexto = {"parques": parques}
    return render(request, "parques/actividades.html", contexto)


def contacto(request):
    enviado = False
    if request.method == "POST":
        # Aquí solo se simula el envío (no hay modelo ni base de datos)
        enviado = True
    return render(request, "parques/contacto.html", {"enviado": enviado})

# Create your views here.
