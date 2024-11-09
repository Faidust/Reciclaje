from django.urls import path
from . import views

urlpatterns=[
    path("reciclar/", views.maps, name="reciclaje"),
    path("plastico/", views.plastico, name="plastico"),
    path("carton/", views.carton, name="carton"),
    path("latas/", views.latas, name="latas"),
    path("vidrio/", views.vidrio, name="vidrio"),
    path("papel/", views.papel, name="papel"),
    path("latas aluminio/", views.latasal, name="latasal"),
    path("tapas/", views.tapas, name="tapas"),
    path("electro/", views.electro, name="electro"),
]