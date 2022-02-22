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


mapp = folium.Map(location=[55.955207,-3.212181], zoom_start=15, tiles='cartodbdark_matter')
folium.TileLayer('openstreetmap', name ='I need help').add_to(mapp)
mapp.add_child(MeasureControl())
folium.LayerControl().add_to(mapp)

conn = cx_Oracle.connect(dsn="geoslearn",user="s1737656",password=pw)
c = conn.cursor()

c.execute("SELECT A.POINT_NAME, SDO_UTIL.TO_WKTGEOMETRY(A.ORA_GEOMETRY), SDO_UTIL.TO_WKTGEOMETRY(B.ORA_GEOMETRY) FROM POINTS_GAME A, POLYGONS_GAME B  WHERE A.POINT_NAME = 'St Bernards Well' AND B.POLY_NAME IN ('Dean Village', 'St Stephens Church')")


for row in c:

    #plot the point(s)
    rname= row[0]
    r4 = row[1].read()
    ro4=r4[7:-1]
    ros4= ro4.split()
    folium.Marker(
            location =[float(ros4[1]), float(ros4[0])],
            icon = folium.Icon(color = 'blue', prefix='glyphicon', icon = 'question-sign'), popup = rname).add_to(mapp)


    r2 = row[2].read()
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
    
    folium.vector_layers.Polygon(locarray2).add_to(mapp)


    

print("Content-type: text/html\n")
print(mapp.get_root().render())
