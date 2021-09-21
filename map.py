import folium


jsonF = 'lim.json'


ateCr = {
    "Ecole d'Ars": (46.004588816648365, 2.07823209410532),  
    
    "Groupe Scolaire Tristan L'Hermite La Souterraine":(46.241512238858995, 1.497249553231962),
    
}

ateHv = {
  "Ecole Hubert Reeves de Rochechouart": (45.82657378874383, 0.824769062099674),
  "Ecole de Saint-Priest-sous-Aixe":(45.85866040256391, 1.0781184014792002),
  "Ecole de Châteauneuf-la-Forêt": (45.71474489300359, 1.6050702463123152),
  "Ecole de Linards": (45.70023005011598, 1.5360591255949927),
  "Ecole de Saint-Sylvestre": (45.99491881835692, 1.3752810163783855),    
 
    
    
    }

ateCo = {
    "Ecole des Lucioles, Beynat": (45.12346911095499, 1.7245924758351892),
    "Ecole primaire d'Argentat-sur-Dordogne": (45.12863668033275, 1.947724198598033),
    "Ecole de Chamboulive":(45.43368577589788, 1.7015756936403286),
    "Ecole Saint-Martin-la-Méanne": (45.167972537996334, 1.9869569118374142),
    
}


m = folium.Map(location=[45.8353810752457, 1.255363987275616], zoom_start=8)
folium.GeoJson(jsonF, name="geojson", tooltip="Académie de Limoges").add_to(m)
for ateE, coords in ateE.items():
    folium.Marker(coords,
                  popup=f'<b>{ ateE }</b><br>{ coords }',
                  tooltip=f'<b>ATE Creuse</b><br>{ ateE }',
                  icon=folium.Icon(color='white', icon_color='#34ff33', icon='fa-tree', prefix='fa'),

                  ).add_to(m)

for ateCr, coordc in ateF.items():
    folium.Marker(coordc,
                  popup=f'<b>{ ateF }</b><br>{ coordc }',
                  tooltip=f'<b>ATE Co</b><br>{ ateF }',
                  icon=folium.Icon(color='lightblue', icon_color='#085a08', icon='fa-tree', prefix='fa'),

           ).add_to(m)
    
for ateHv, coordc in ateF.items():
    folium.Marker(coordc,
                  popup=f'<b>{ ateF }</b><br>{ coordc }',
                  tooltip=f'<b>ATE Haute Vienne</b><br>{ ateF }',
                  icon=folium.Icon(color='lightpink', icon_color='#085a08', icon='fa-tree', prefix='fa'),

           ).add_to(m)
  
    
for ateCo, coordc in ateF.items():
    folium.Marker(coordc,
                  popup=f'<b>{ ateF }</b><br>{ coordc }',
                  tooltip=f'<b>ATE Corrèze</b><br>{ ateF }',
                  icon=folium.Icon(color='lightgreen', icon_color='#FFB6C1', icon='fa-tree', prefix='fa'),

           ).add_to(m)

m.save('templates/ate.html')
