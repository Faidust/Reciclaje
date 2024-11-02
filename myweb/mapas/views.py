from django.shortcuts import render
import folium

def maps(request):
    return render(request,'reciclar.html')

def plastico(request):
    texto_plastico="<h1>Patio principal</h1>"
    min_lon, max_lon = -70.62020630592322, -70.61816934867323
    min_lat, max_lat = -33.491713968794016, -33.489445772654996
    initialmap= folium.Map(max_bounds=True, location=[-33.49061291008033, -70.61921242455158], zoom_start=18,min_lat=min_lat, max_lat=max_lat, min_lon=min_lon, max_lon=max_lon)
    folium.Marker(location=[-33.490106475860095, -70.61868275699759],popup=texto_plastico).add_to(initialmap)
    folium.CircleMarker([max_lat, min_lon], tooltip="Upper Left Corner").add_to(initialmap)
    folium.CircleMarker([min_lat, min_lon], tooltip="Lower Left Corner").add_to(initialmap)
    folium.CircleMarker([min_lat, max_lon], tooltip="Lower Right Corner").add_to(initialmap)
    folium.CircleMarker([max_lat, max_lon], tooltip="Upper Right Corner").add_to(initialmap)
    context={"mapas":initialmap._repr_html_()}
    return render(request,'plastico.html',context)

def carton(request):
    texto_carton="<h1>Patio principal</h1>"
    min_lon, max_lon = -70.62020630592322, -70.61816934867323
    min_lat, max_lat = -33.491713968794016, -33.489445772654996
    initialmap= folium.Map(max_bounds=True, location=[-33.49061291008033, -70.61921242455158], zoom_start=18,min_lat=min_lat, max_lat=max_lat, min_lon=min_lon, max_lon=max_lon)
    folium.Marker(location=[-33.490106475860095, -70.61868275699759],popup=texto_carton).add_to(initialmap)
    folium.CircleMarker([max_lat, min_lon], tooltip="Upper Left Corner").add_to(initialmap)
    folium.CircleMarker([min_lat, min_lon], tooltip="Lower Left Corner").add_to(initialmap)
    folium.CircleMarker([min_lat, max_lon], tooltip="Lower Right Corner").add_to(initialmap)
    folium.CircleMarker([max_lat, max_lon], tooltip="Upper Right Corner").add_to(initialmap)
    context={"mapas":initialmap._repr_html_()}
    return render(request,'carton.html',context)