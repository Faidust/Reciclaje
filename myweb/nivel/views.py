
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Palabra, Reciclaje
from django.db.models import Sum


@login_required
def nivel(request):
    total_palabras = Palabra.objects.filter(usuario=request.user).aggregate(Sum('cantidad'))['cantidad__sum'] or 0
    return render(request, "nivel.html", {'total_palabras': total_palabras})


@login_required
def guardar_palabra(request):
    if request.method == 'POST':
        palabra = request.POST['palabra']
        usuario = request.user
        Palabra_obj, created = Palabra.objects.get_or_create(usuario=usuario, Palabra=palabra)
        Palabra_obj.cantidad += 1
        Palabra_obj.save()
        
    return redirect('usuariodos')
    

@login_required
def usuariodos(request):
    usuario = request.user
    palabras = Palabra.objects.filter(usuario=request.user)
    ultimas_palabras = palabras.order_by('-id')[:3]
    total_palabras = Palabra.objects.filter(usuario=request.user).aggregate(Sum('cantidad'))['cantidad__sum'] or 0
    numnivel = 0
    if total_palabras <= 5:  # Por ejemplo, cada 10 palabras
        numnivel += 1
        nombrenivel = "Iniciador de Cambios"

    elif total_palabras <= 10:
        numnivel += 2
        nombrenivel = "Aprendiz"
    elif total_palabras <= 15:
        numnivel += 3
        nombrenivel = "Maestro"
    else:
        numnivel +=4
        nombrenivel = "Guerrero comprometido"
    return render(request, 'nivel.html', {
        'palabras': palabras,
        'ultimas_palabras': ultimas_palabras,
        'usuario': usuario,
        'total_palabras': total_palabras,
        'nombrenivel': nombrenivel,
        'numnivel': numnivel
        
    })
