
from django.urls import path
from . import views

urlpatterns=[
    path('nivel/', views.nivel, name='nivel'),
    path('guardar_palabra/', views.guardar_palabra, name='guardar_palabra'),
    path('usuariodos/', views.usuariodos, name='usuariodos'),

]
