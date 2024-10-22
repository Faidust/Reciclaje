from django.shortcuts import render
import folium

def maps(request):
    return render(request,'reciclar.html')

def plastico(request):
    initialmap= folium.Map(location=[-33.49061291008033, -70.61921242455158], zoom_start=19)
    context={"mapas":initialmap._repr_html_()}
    return render(request,'plastico.html',context)
