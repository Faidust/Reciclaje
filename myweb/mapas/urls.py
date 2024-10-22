from django.urls import path
from . import views

urlpatterns=[
    path("reciclar/", views.maps, name="reciclaje"),
    path("plastico/", views.plastico, name="plastico"),
]