from django.urls import path
from . import views 

urlpatterns=[
    path('', views.index, name="home"),
    path("inicio/", views.inicio, name="inicio")
]