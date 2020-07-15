import folium #importing folium package for maps        #Download by 'pip install folium'
import pandas #importing pandas for reading csv files           #Download by 'pip install pandas' 

data = pandas.read_csv("Valcanoes.txt") #Reading csv file for getting values of latitude, longtitude, elevation
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):      #Using function for getting the spectific colors for spotting the valcanoes by height
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation <3000:
        return 'orange'
    else:
        return 'red'
        
map = folium.Map(location = [10,77],zoom_start=6, tiles="Stamen Terrain") #Creating the map object

fgv=folium.FeatureGroup(name="Valcanoes") #creating the FeatureGroup for Valcanoes

for lt, ln, el in zip(lat, lon, elev):  #Plotting the points with different colors based on height using loop
     fgv.add_child(folium.CircleMarker(location=[lt, ln],popup=str(el)+ " m"
                                      ,fill_color=color_producer(el), color = 'grey'
                                      ,fill_opacity = 0.7))

fgp = folium.FeatureGroup(name="Population")#Creating the FeatureGroup for Population

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),  #Plotting the country lines on the map and filling the color by pop;ulation
                             style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
                                                       else 'orange' if 10000000 <= x['properties']['POP2005'] <20000000
                                                       else 'red'}))

map.add_child(fgv)  #Adding the feature group to the map object
map.add_child(fgp)
map.add_child(folium.LayerControl())  #Adding the layer control option to the map

map.save("Map1.html") #Saving the file as a html file for executing
