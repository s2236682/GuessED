#!/usr/bin/env python3
import cgi
import cgitb
import folium
import numpy as np
import cx_Oracle
from folium.plugins import MeasureControl

cgitb.enable()

with open("../../nadaa",'r') as pwf:
    pw = pwf.read().strip()


mapp = folium.Map(location=[55.952319, -3.217860], zoom_start=17, tiles='cartodbdark_matter')
folium.TileLayer('openstreetmap', name ='I need help').add_to(mapp)
mapp.add_child(MeasureControl())
folium.LayerControl().add_to(mapp)

conn = cx_Oracle.connect(dsn="geoslearn",user="s1737656",password=pw)
c = conn.cursor()

c.execute("SELECT SDO_UTIL.TO_WKTGEOMETRY(ORA_GEOMETRY) FROM POLYGONS_GAME WHERE POLY_NAME = 'Dean Village'")


for row in c:
 
    r2 = row[0].read()
    ro2=r2[10:-2]
    ros2= ro2.split(",")
    location2 = []
    for i in ros2:
        l= i.split()
        location2.append((float(l[1]), float(l[0])))
        
    locarray2= []
    for i in location2:
        lista=[*i]
        locarray2.append(lista)
    
    folium.vector_layers.Polygon(locarray2, popup=" What is this polygon?").add_to(mapp)


print("Content-type: text/html\n")
print(mapp.get_root().render())
