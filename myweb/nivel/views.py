
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Palabra, Reciclaje


@login_required
def nivel(request):
    return render(request, "nivel.html")

@login_required
def guardar_palabra(request):
    if request.method == 'POST':
        material = request.POST.get('palabra')
        usuario = request.user
        models = Palabra(usuario=usuario, Palabra=material)
        '''palabra_obj, created = Palabra.OBJECT.get_or_create(usuario=usuario, palabra=Palabra)
        palabra_obj.cantidad += 1
        palabra_obj.save()'''
        models.save()
        return redirect('usuariodos')
    return render(request, 'nivel.html')

@login_required
def usuariodos(request):
    palabras = Palabra.objects.filter(usuario=request.user)
    total_palabras = sum(Palabra.cantidad for palabra in palabras)
    return render(request, 'nivel.html', {'palabras': palabras, 'total_palabras': total_palabras})
# Create your views here.
