import folium


jsonF = 'lim.json'


ateE = {
    "Ecole d'Ars": (46.004588816648365, 2.07823209410532),
    "Ecole des Lucioles, Beynat": (45.12346911095499, 1.7245924758351892),
    "Ecole de Saint-Sylvestre": (45.99491881835692, 1.3752810163783855),
    "Ecole Hubert Reeves de Rochechouart": (45.82657378874383, 0.824769062099674),



}

ateF = {
    "Ecole de Lussat": (46.18325300746391, 2.3410375477839938),
    "Collège Marouzeau": (46.16664629793548, 1.8706000026445602),
    "Ecole Saint-Martin-la-Méanne": (45.167972537996334, 1.9869569118374142),
    "Ecole de Saint-Priest-sous-Aixe":(45.85866040256391, 1.0781184014792002),
    "Ecoles du secteur de Châteauneuf-la-Forêt": (45.71474489300359, 1.6050702463123152),
    "Ecole de Saint Bonnet de Bellac": (46.16925655629941, 0.9533716117326017),
    "Ecole primaire d'Argentat-sur-Dordogne": (45.12863668033275, 1.947724198598033),
    "Ecole primaire de Gorre": (45.74537464516415, 0.9850259572576966)
    }


m = folium.Map(location=[45.8353810752457, 1.255363987275616], zoom_start=8)
folium.GeoJson(jsonF, name="geojson", tooltip="Académie de Limoges").add_to(m)
for ateE, coords in ateE.items():
    folium.Marker(coords,
                  popup=f'<b>{ ateE }</b><br>{ coords }',
                  tooltip=f'<b>ATE existante</b><br>{ ateE }',
                  icon=folium.Icon(color='white', icon_color='#34ff33', icon='fa-tree', prefix='fa'),

                  ).add_to(m)

for ateF, coordc in ateF.items():
    folium.Marker(coordc,
                  popup=f'<b>{ ateF }</b><br>{ coordc }',
                  tooltip=f'<b>ATE en projet</b><br>{ ateF }',
                  icon=folium.Icon(color='lightblue', icon_color='#085a08', icon='fa-plus-square-o', prefix='fa'),

           ).add_to(m)

m.save('templates/ate.html')
