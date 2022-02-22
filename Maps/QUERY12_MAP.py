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


mapp = folium.Map(location=[55.955511,-3.211658], zoom_start=18, tiles='cartodbdark_matter')
folium.TileLayer('openstreetmap', name ='I need help').add_to(mapp)
mapp.add_child(MeasureControl())
folium.LayerControl().add_to(mapp)

conn = cx_Oracle.connect(dsn="geoslearn",user="s1737656",password=pw)
c = conn.cursor()

c.execute("SELECT SDO_UTIL.TO_WKTGEOMETRY(A.ORA_GEOMETRY), B.ROUTE_NAME, SDO_UTIL.TO_WKTGEOMETRY(B.ORA_GEOMETRY) FROM POINTS_GAME A, ROUTES_GAME B, ROUTES_GAME C WHERE B.ROUTE_NAME = 'Water of Leith'")


for row in c:
    #point
    r4 = row[0].read()
    ro4=r4[7:-1]
    ros4= ro4.split()
    folium.Marker(
            location =[float(ros4[1]), float(ros4[0])],
            icon = folium.Icon(color = 'blue', prefix='glyphicon', icon = 'question-sign')).add_to(mapp)

    
    #polyline
    name3=row[1]
    r3 = row[2].read()
    ro3=r3[12:-1]
    ros3= ro3.split(",")
    location3 = []
    for i in ros3:
        lala = i.split()
        location3.append((float(lala[1]), float(lala[0])))
        
    locarray3= []
    for i in location3:
        lista=[*i]
        locarray3.append(lista)
    folium.vector_layers.PolyLine(locarray3, popup=name3).add_to(mapp)

 

print("Content-type: text/html\n")
print(mapp.get_root().render())
