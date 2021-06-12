import folium
import pandas as pd

df = pd.read_csv('Volcanoes.txt')
lat = list(df['LAT'])
lon = list(df['LON'])
ele = list(df['ELEV'])

def elevation(el):
    if el <2000:
        return 'blue'
    elif 2000<= el <=3500:
        return 'beige'
    else:
        return 'darkred' 


map = folium.Map(location=[47.2510994,-123.1254764], zoom_start=6, tiles ='Stamen Terrain' )
fg = folium.FeatureGroup(name='My map')
for lt, ln, el in zip(lat,lon,ele):
    fg.add_child(folium.CircleMarker(location=[lt,ln] , popup = str(el) + ' Meter', radius = 10, fill_color= 
    elevation(el), color = 'black', fill_opacity = 0.7))
map.add_child(fg)
map.save('Map1.html')