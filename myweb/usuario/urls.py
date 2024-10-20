from django.urls import path
from . import views

urlpatterns=[
    path("usuario/", views.usuario, name="usuario"),
    path("logout/", views.exit),
    path("register/", views.register, name="register"),
]