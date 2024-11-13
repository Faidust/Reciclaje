from django.shortcuts import render
import folium

def maps(request):
    return render(request,'reciclar.html')

def plastico(request):
    texto_plastico="<h1>Patio principal</h1>"
    entrada1="<h1>Pasillo entrada principal</h1>"
    noac="<h1>Entrada noac</h1>"
    pasillob="<h1>Pasillo salas b</h1>"
    labinf="<h1>Pasillo laboratorios de informática</h1>"
    labpro="<h1>Frente a laboratorio de procesos</h1>"
    entradak="<h1>Entrada edificio K</h1>"
    pisoinferior1="<h1>Piso -1 edificio K</h1>"
    pisoinferior2="<h1>Piso -2 edificio K</h1>"
    pisosuperior1="<h1>Piso 2 edificio K</h1>"
    pisosuperior2="<h1>Piso 3 edificio K</h1>"
    pisosuperior3="<h1>Piso 4 edificio K</h1>"
    fablab="<h1>Frente al fablab</h1>"
    piso4="<h1>Piso 4 edificio F</h1>"
    min_lon, max_lon = -70.62020630592322, -70.61816934867323
    min_lat, max_lat = -33.491713968794016, -33.489445772654996
    initialmap= folium.Map(max_bounds=True, location=[-33.49061291008033, -70.61921242455158], zoom_start=18,min_lat=min_lat, max_lat=max_lat, min_lon=min_lon, max_lon=max_lon)
    folium.Marker(location=[-33.490106475860095, -70.61868275699759],popup=texto_plastico).add_to(initialmap)
    folium.Marker(location=[-33.49111872651402, -70.61828921141128],popup=entrada1).add_to(initialmap)
    folium.Marker(location=[-33.490746887805294, -70.618373805988],popup=entrada1).add_to(initialmap)
    folium.Marker(location=[-33.48967631544855, -70.61887387051037],popup=noac).add_to(initialmap)
    folium.Marker(location=[-33.48981692868987, -70.61947739663124],popup=pasillob).add_to(initialmap)
    folium.Marker(location=[-33.49006300131277, -70.61951379979408],popup=labinf).add_to(initialmap)
    folium.Marker(location=[-33.48989362672521, -70.62012690570444],popup=labpro).add_to(initialmap)
    folium.Marker(location=[-33.491421808964375, -70.61953094458248],popup=entradak).add_to(initialmap)
    folium.Marker(location=[-33.491362435311125, -70.61894608414818],popup=pisoinferior1).add_to(initialmap)
    folium.Marker(location=[-33.4912947705664, -70.61894775751142],popup=pisoinferior2).add_to(initialmap)
    folium.Marker(location=[-33.49160165259362, -70.61885407218092],popup=pisoinferior1).add_to(initialmap)
    folium.Marker(location=[-33.49165250946155, -70.61933704889559],popup=pisoinferior1).add_to(initialmap)
    folium.Marker(location=[-33.49157927556227, -70.61945413415974],popup=pisosuperior1).add_to(initialmap)
    folium.Marker(location=[-33.49151011015608, -70.61886139000993],popup=pisosuperior2).add_to(initialmap)
    folium.Marker(location=[-33.49145721892583, -70.61892968974736],popup=pisosuperior3).add_to(initialmap)
    folium.Marker(location=[-33.49155486424875, -70.6191980101444],popup=pisosuperior3).add_to(initialmap)
    folium.Marker(location=[-33.490950682046076, -70.61869795849537],popup=fablab).add_to(initialmap)
    folium.Marker(location=[-33.49055196016342, -70.61957121942228],popup=piso4).add_to(initialmap)
    folium.Marker(location=[-33.49049296544408, -70.61872235125712],popup=piso4).add_to(initialmap)
    folium.CircleMarker([max_lat, min_lon], tooltip="Upper Left Corner").add_to(initialmap)
    folium.CircleMarker([min_lat, min_lon], tooltip="Lower Left Corner").add_to(initialmap)
    folium.CircleMarker([min_lat, max_lon], tooltip="Lower Right Corner").add_to(initialmap)
    folium.CircleMarker([max_lat, max_lon], tooltip="Upper Right Corner").add_to(initialmap)
    context={"mapas":initialmap._repr_html_()}
    return render(request,'plastico.html',context)

def carton(request):
    texto_carton="<h1>Patio principal</h1>"
    entrada1="<h1>Pasillo entrada principal</h1>"
    noac="<h1>Entrada noac</h1>"
    labinf="<h1>Pasillo laboratorios de informática</h1>"
    labpro="<h1>Frente a laboratorio de procesos</h1>"
    entradak="<h1>Entrada edificio K</h1>"
    pisoinferior1="<h1>Piso -1 edificio K</h1>"
    pisoinferior2="<h1>Piso -2 edificio K</h1>"
    pisosuperior1="<h1>Piso 2 edificio K</h1>"
    pisosuperior2="<h1>Piso 3 edificio K</h1>"
    pisosuperior3="<h1>Piso 4 edificio K</h1>"
    fablab="<h1>Frente al fablab</h1>"
    piso4="<h1>Piso 4 edificio F</h1>"
    min_lon, max_lon = -70.62020630592322, -70.61816934867323
    min_lat, max_lat = -33.491713968794016, -33.489445772654996
    initialmap= folium.Map(max_bounds=True, location=[-33.49061291008033, -70.61921242455158], zoom_start=18,min_lat=min_lat, max_lat=max_lat, min_lon=min_lon, max_lon=max_lon)
    folium.Marker(location=[-33.490106475860095, -70.61868275699759],popup=texto_carton).add_to(initialmap)
    folium.Marker(location=[-33.49111872651402, -70.61828921141128],popup=entrada1).add_to(initialmap)
    folium.Marker(location=[-33.490746887805294, -70.618373805988],popup=entrada1).add_to(initialmap)
    folium.Marker(location=[-33.48967631544855, -70.61887387051037],popup=noac).add_to(initialmap)
    folium.Marker(location=[-33.49006300131277, -70.61951379979408],popup=labinf).add_to(initialmap)
    folium.Marker(location=[-33.48989362672521, -70.62012690570444],popup=labpro).add_to(initialmap)
    folium.Marker(location=[-33.491421808964375, -70.61953094458248],popup=entradak).add_to(initialmap)
    folium.Marker(location=[-33.491362435311125, -70.61894608414818],popup=pisoinferior1).add_to(initialmap)
    folium.Marker(location=[-33.4912947705664, -70.61894775751142],popup=pisoinferior2).add_to(initialmap)
    folium.Marker(location=[-33.49160165259362, -70.61885407218092],popup=pisoinferior1).add_to(initialmap)
    folium.Marker(location=[-33.49165250946155, -70.61933704889559],popup=pisoinferior1).add_to(initialmap)
    folium.Marker(location=[-33.49157927556227, -70.61945413415974],popup=pisosuperior1).add_to(initialmap)
    folium.Marker(location=[-33.49151011015608, -70.61886139000993],popup=pisosuperior2).add_to(initialmap)
    folium.Marker(location=[-33.49145721892583, -70.61892968974736],popup=pisosuperior3).add_to(initialmap)
    folium.Marker(location=[-33.49155486424875, -70.6191980101444],popup=pisosuperior3).add_to(initialmap)
    folium.Marker(location=[-33.490950682046076, -70.61869795849537],popup=fablab).add_to(initialmap)
    folium.Marker(location=[-33.49055196016342, -70.61957121942228],popup=piso4).add_to(initialmap)
    folium.Marker(location=[-33.49049296544408, -70.61872235125712],popup=piso4).add_to(initialmap)
    folium.CircleMarker([max_lat, min_lon], tooltip="Upper Left Corner").add_to(initialmap)
    folium.CircleMarker([min_lat, min_lon], tooltip="Lower Left Corner").add_to(initialmap)
    folium.CircleMarker([min_lat, max_lon], tooltip="Lower Right Corner").add_to(initialmap)
    folium.CircleMarker([max_lat, max_lon], tooltip="Upper Right Corner").add_to(initialmap)
    context={"mapas":initialmap._repr_html_()}
    return render(request,'carton.html',context)

def latas(request):
    texto_carton="<h1>Patio principal</h1>"
    entrada1="<h1>Pasillo entrada principal</h1>"
    noac="<h1>Entrada noac</h1>"
    labinf="<h1>Pasillo laboratorios de informática</h1>"
    labpro="<h1>Frente a laboratorio de procesos</h1>"
    entradak="<h1>Entrada edificio K</h1>"
    pisoinferior1="<h1>Piso -1 edificio K</h1>"
    pisoinferior2="<h1>Piso -2 edificio K</h1>"
    pisosuperior2="<h1>Piso 3 edificio K</h1>"
    pisosuperior3="<h1>Piso 4 edificio K</h1>"
    fablab="<h1>Frente al fablab</h1>"
    piso4="<h1>Piso 4 edificio F</h1>"
    min_lon, max_lon = -70.62020630592322, -70.61816934867323
    min_lat, max_lat = -33.491713968794016, -33.489445772654996
    initialmap= folium.Map(max_bounds=True, location=[-33.49061291008033, -70.61921242455158], zoom_start=18,min_lat=min_lat, max_lat=max_lat, min_lon=min_lon, max_lon=max_lon)
    folium.Marker(location=[-33.490106475860095, -70.61868275699759],popup=texto_carton).add_to(initialmap)
    folium.Marker(location=[-33.49111872651402, -70.61828921141128],popup=entrada1).add_to(initialmap)
    folium.Marker(location=[-33.490746887805294, -70.618373805988],popup=entrada1).add_to(initialmap)
    folium.Marker(location=[-33.48967631544855, -70.61887387051037],popup=noac).add_to(initialmap)
    folium.Marker(location=[-33.49006300131277, -70.61951379979408],popup=labinf).add_to(initialmap)
    folium.Marker(location=[-33.48989362672521, -70.62012690570444],popup=labpro).add_to(initialmap)
    folium.Marker(location=[-33.491421808964375, -70.61953094458248],popup=entradak).add_to(initialmap)
    folium.Marker(location=[-33.4912947705664, -70.61894775751142],popup=pisoinferior2).add_to(initialmap)
    folium.Marker(location=[-33.49165250946155, -70.61933704889559],popup=pisoinferior1).add_to(initialmap)
    folium.Marker(location=[-33.49151011015608, -70.61886139000993],popup=pisosuperior2).add_to(initialmap)
    folium.Marker(location=[-33.49145721892583, -70.61892968974736],popup=pisosuperior3).add_to(initialmap)
    folium.Marker(location=[-33.49155486424875, -70.6191980101444],popup=pisosuperior3).add_to(initialmap)
    folium.Marker(location=[-33.490950682046076, -70.61869795849537],popup=fablab).add_to(initialmap)
    folium.Marker(location=[-33.49055196016342, -70.61957121942228],popup=piso4).add_to(initialmap)
    folium.Marker(location=[-33.49049296544408, -70.61872235125712],popup=piso4).add_to(initialmap)
    folium.CircleMarker([max_lat, min_lon], tooltip="Upper Left Corner").add_to(initialmap)
    folium.CircleMarker([min_lat, min_lon], tooltip="Lower Left Corner").add_to(initialmap)
    folium.CircleMarker([min_lat, max_lon], tooltip="Lower Right Corner").add_to(initialmap)
    folium.CircleMarker([max_lat, max_lon], tooltip="Upper Right Corner").add_to(initialmap)
    context={"mapas":initialmap._repr_html_()}
    return render(request,'latas.html',context)

def vidrio(request):
    texto_carton="<h1>Patio principal</h1>"
    entrada1="<h1>Pasillo entrada principal</h1>"
    noac="<h1>Entrada noac</h1>"
    pasillob="<h1>Pasillo salas b</h1>"
    labinf="<h1>Pasillo laboratorios de informática</h1>"
    labpro="<h1>Frente a laboratorio de procesos</h1>"
    entradak="<h1>Entrada edificio K</h1>"
    pisoinferior1="<h1>Piso -1 edificio K</h1>"
    pisoinferior2="<h1>Piso -2 edificio K</h1>"
    pisosuperior1="<h1>Piso 2 edificio K</h1>"
    pisosuperior2="<h1>Piso 3 edificio K</h1>"
    pisosuperior3="<h1>Piso 4 edificio K</h1>"
    fablab="<h1>Frente al fablab</h1>"
    piso4="<h1>Piso 4 edificio F</h1>"
    min_lon, max_lon = -70.62020630592322, -70.61816934867323
    min_lat, max_lat = -33.491713968794016, -33.489445772654996
    initialmap= folium.Map(max_bounds=True, location=[-33.49061291008033, -70.61921242455158], zoom_start=18,min_lat=min_lat, max_lat=max_lat, min_lon=min_lon, max_lon=max_lon)
    folium.Marker(location=[-33.490106475860095, -70.61868275699759],popup=texto_carton).add_to(initialmap)
    folium.Marker(location=[-33.49111872651402, -70.61828921141128],popup=entrada1).add_to(initialmap)
    folium.Marker(location=[-33.490746887805294, -70.618373805988],popup=entrada1).add_to(initialmap)
    folium.Marker(location=[-33.48967631544855, -70.61887387051037],popup=noac).add_to(initialmap)
    folium.Marker(location=[-33.48981692868987, -70.61947739663124],popup=pasillob).add_to(initialmap)
    folium.Marker(location=[-33.49006300131277, -70.61951379979408],popup=labinf).add_to(initialmap)
    folium.Marker(location=[-33.48989362672521, -70.62012690570444],popup=labpro).add_to(initialmap)
    folium.Marker(location=[-33.491421808964375, -70.61953094458248],popup=entradak).add_to(initialmap)
    folium.Marker(location=[-33.491362435311125, -70.61894608414818],popup=pisoinferior1).add_to(initialmap)
    folium.Marker(location=[-33.4912947705664, -70.61894775751142],popup=pisoinferior2).add_to(initialmap)
    folium.Marker(location=[-33.49160165259362, -70.61885407218092],popup=pisoinferior1).add_to(initialmap)
    folium.Marker(location=[-33.49165250946155, -70.61933704889559],popup=pisoinferior1).add_to(initialmap)
    folium.Marker(location=[-33.49157927556227, -70.61945413415974],popup=pisosuperior1).add_to(initialmap)
    folium.Marker(location=[-33.49151011015608, -70.61886139000993],popup=pisosuperior2).add_to(initialmap)
    folium.Marker(location=[-33.49145721892583, -70.61892968974736],popup=pisosuperior3).add_to(initialmap)
    folium.Marker(location=[-33.490950682046076, -70.61869795849537],popup=fablab).add_to(initialmap)
    folium.Marker(location=[-33.49055196016342, -70.61957121942228],popup=piso4).add_to(initialmap)
    folium.Marker(location=[-33.49049296544408, -70.61872235125712],popup=piso4).add_to(initialmap)
    folium.CircleMarker([max_lat, min_lon], tooltip="Upper Left Corner").add_to(initialmap)
    folium.CircleMarker([min_lat, min_lon], tooltip="Lower Left Corner").add_to(initialmap)
    folium.CircleMarker([min_lat, max_lon], tooltip="Lower Right Corner").add_to(initialmap)
    folium.CircleMarker([max_lat, max_lon], tooltip="Upper Right Corner").add_to(initialmap)
    context={"mapas":initialmap._repr_html_()}
    return render(request,'vidrio.html',context)

def papel(request):
    texto_carton="<h1>Patio principal</h1>"
    entrada1="<h1>Pasillo entrada principal</h1>"
    noac="<h1>Entrada noac</h1>"
    labinf="<h1>Pasillo laboratorios de informática</h1>"
    labpro="<h1>Frente a laboratorio de procesos</h1>"
    entradak="<h1>Entrada edificio K</h1>"
    pisoinferior1="<h1>Piso -1 edificio K</h1>"
    pisoinferior2="<h1>Piso -2 edificio K</h1>"
    pisosuperior1="<h1>Piso 2 edificio K</h1>"
    pisosuperior2="<h1>Piso 3 edificio K</h1>"
    pisosuperior3="<h1>Piso 4 edificio K</h1>"
    fablab="<h1>Frente al fablab</h1>"
    piso4="<h1>Piso 4 edificio F</h1>"
    min_lon, max_lon = -70.62020630592322, -70.61816934867323
    min_lat, max_lat = -33.491713968794016, -33.489445772654996
    initialmap= folium.Map(max_bounds=True, location=[-33.49061291008033, -70.61921242455158], zoom_start=18,min_lat=min_lat, max_lat=max_lat, min_lon=min_lon, max_lon=max_lon)
    folium.Marker(location=[-33.490106475860095, -70.61868275699759],popup=texto_carton).add_to(initialmap)
    folium.Marker(location=[-33.49111872651402, -70.61828921141128],popup=entrada1).add_to(initialmap)
    folium.Marker(location=[-33.490746887805294, -70.618373805988],popup=entrada1).add_to(initialmap)
    folium.Marker(location=[-33.48967631544855, -70.61887387051037],popup=noac).add_to(initialmap)
    folium.Marker(location=[-33.49006300131277, -70.61951379979408],popup=labinf).add_to(initialmap)
    folium.Marker(location=[-33.48989362672521, -70.62012690570444],popup=labpro).add_to(initialmap)
    folium.Marker(location=[-33.491421808964375, -70.61953094458248],popup=entradak).add_to(initialmap)
    folium.Marker(location=[-33.491362435311125, -70.61894608414818],popup=pisoinferior1).add_to(initialmap)
    folium.Marker(location=[-33.4912947705664, -70.61894775751142],popup=pisoinferior2).add_to(initialmap)
    folium.Marker(location=[-33.49160165259362, -70.61885407218092],popup=pisoinferior1).add_to(initialmap)
    folium.Marker(location=[-33.49165250946155, -70.61933704889559],popup=pisoinferior1).add_to(initialmap)
    folium.Marker(location=[-33.49157927556227, -70.61945413415974],popup=pisosuperior1).add_to(initialmap)
    folium.Marker(location=[-33.49151011015608, -70.61886139000993],popup=pisosuperior2).add_to(initialmap)
    folium.Marker(location=[-33.49145721892583, -70.61892968974736],popup=pisosuperior3).add_to(initialmap)
    folium.Marker(location=[-33.49155486424875, -70.6191980101444],popup=pisosuperior3).add_to(initialmap)
    folium.Marker(location=[-33.490950682046076, -70.61869795849537],popup=fablab).add_to(initialmap)
    folium.Marker(location=[-33.49055196016342, -70.61957121942228],popup=piso4).add_to(initialmap)
    folium.Marker(location=[-33.49049296544408, -70.61872235125712],popup=piso4).add_to(initialmap)
    folium.CircleMarker([max_lat, min_lon], tooltip="Upper Left Corner").add_to(initialmap)
    folium.CircleMarker([min_lat, min_lon], tooltip="Lower Left Corner").add_to(initialmap)
    folium.CircleMarker([min_lat, max_lon], tooltip="Lower Right Corner").add_to(initialmap)
    folium.CircleMarker([max_lat, max_lon], tooltip="Upper Right Corner").add_to(initialmap)
    context={"mapas":initialmap._repr_html_()}
    return render(request,'papel.html',context)

def tapas(request):
    noac="<h1>Entrada noac</h1>"
    pasillob="<h1>Pasillo salas b</h1>"
    fablab="<h1>Frente al fablab</h1>"
    min_lon, max_lon = -70.62020630592322, -70.61816934867323
    min_lat, max_lat = -33.491713968794016, -33.489445772654996
    initialmap= folium.Map(max_bounds=True, location=[-33.49061291008033, -70.61921242455158], zoom_start=18,min_lat=min_lat, max_lat=max_lat, min_lon=min_lon, max_lon=max_lon)
    folium.Marker(location=[-33.48967631544855, -70.61887387051037],popup=noac).add_to(initialmap)
    folium.Marker(location=[-33.48981692868987, -70.61947739663124],popup=pasillob).add_to(initialmap)
    folium.Marker(location=[-33.490950682046076, -70.61869795849537],popup=fablab).add_to(initialmap)
    folium.CircleMarker([max_lat, min_lon], tooltip="Upper Left Corner").add_to(initialmap)
    folium.CircleMarker([min_lat, min_lon], tooltip="Lower Left Corner").add_to(initialmap)
    folium.CircleMarker([min_lat, max_lon], tooltip="Lower Right Corner").add_to(initialmap)
    folium.CircleMarker([max_lat, max_lon], tooltip="Upper Right Corner").add_to(initialmap)
    context={"mapas":initialmap._repr_html_()}
    return render(request,'tapas.html',context)

def electro(request):
    pasillob="<h1>Pasillo salas b</h1>"
    fablab="<h1>Frente al fablab</h1>"
    min_lon, max_lon = -70.62020630592322, -70.61816934867323
    min_lat, max_lat = -33.491713968794016, -33.489445772654996
    initialmap= folium.Map(max_bounds=True, location=[-33.49061291008033, -70.61921242455158], zoom_start=18,min_lat=min_lat, max_lat=max_lat, min_lon=min_lon, max_lon=max_lon)
    folium.Marker(location=[-33.48981692868987, -70.61947739663124],popup=pasillob).add_to(initialmap)
    folium.Marker(location=[-33.490950682046076, -70.61869795849537],popup=fablab).add_to(initialmap)
    folium.CircleMarker([max_lat, min_lon], tooltip="Upper Left Corner").add_to(initialmap)
    folium.CircleMarker([min_lat, min_lon], tooltip="Lower Left Corner").add_to(initialmap)
    folium.CircleMarker([min_lat, max_lon], tooltip="Lower Right Corner").add_to(initialmap)
    folium.CircleMarker([max_lat, max_lon], tooltip="Upper Right Corner").add_to(initialmap)
    context={"mapas":initialmap._repr_html_()}
    return render(request,'electro.html',context)