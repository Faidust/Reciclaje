
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Palabra, Reciclaje


@login_required
def nivel(request):
    return render(request, "nivel.html")

@login_required
def guardar_palabra(request):
    if request.method == 'POST':
        cantidad = 0
        palabra = request.POST['palabra']
        usuario = request.user
        Palabra_obj, created = Palabra.objects.get_or_create(usuario=usuario, Palabra=palabra)
        Palabra_obj.cantidad += 1
        Palabra_obj.save()
        numnivel = 0
        nombrenivel = ""
        palabras = Palabra.objects.filter(usuario=request.user)
        total_palabras = palabras.order_by('-id').first().id if palabras.exists() else None
        
        if total_palabras >= 5:  # Por ejemplo, cada 10 palabras
            numnivel += 1
            nombrenivel = "Iniciador de Cambios"

        elif total_palabras >= 10:
            numnivel += 1
            nombrenivel = "Aprendiz"
        elif total_palabras >= 15:
            numnivel += 1
            nombrenivel = "Maestro"
        else:
            numnivel +=1
            nombrenivel = "Guerrero comprometido"
            
    return redirect('usuariodos')
    return render(request, 'nivel.html',{
        'nombrenivel' : nombrenivel
    })

@login_required
def usuariodos(request):
   
    palabras = Palabra.objects.filter(usuario=request.user)
    total_palabras = palabras.order_by('-id').first().id if palabras.exists() else None
    '''return render(request, 'nivel.html', {'palabras': palabras, 'total_palabras': total_palabras})'''
    ultimas_palabras = palabras.order_by('-id')[:3]
    
    return render(request, 'nivel.html', {
        #'usuario': usuario,
        'palabras': palabras,
        'total_palabras': total_palabras,
        'ultimas_palabras': ultimas_palabras,
        
        
    })
