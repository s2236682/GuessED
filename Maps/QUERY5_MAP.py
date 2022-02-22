#!/usr/bin/env python3
import cgi
import cgitb
import folium
import numpy as np
import cx_Oracle
#from folium.plugins import MeasureControl
cgitb.enable()

with open("../../nadaa",'r') as pwf:
    pw = pwf.read().strip()


mapp = folium.Map(location=[55.952623,-3.193122], max_zoom=20, zoom_start=18, tiles='cartodbdark_matter')
#mapp.add_child(MeasureControl())
folium.TileLayer('openstreetmap', name ='I need help').add_to(mapp)
folium.LayerControl().add_to(mapp)

conn = cx_Oracle.connect(dsn="geoslearn",user="s1737656",password=pw)
c = conn.cursor()

c.execute("SELECT A.SP_NAME, SDO_UTIL.TO_WKTGEOMETRY(A.ORA_GEOMETRY), SDO_UTIL.TO_WKTGEOMETRY(B.ORA_GEOMETRY), C.ROUTE_NAME, SDO_UTIL.TO_WKTGEOMETRY(C.ORA_GEOMETRY) FROM SEARCHPOINTS_GAME A, POINTS_GAME B, ROUTES_GAME C WHERE A.SP_NAME = 'E' AND C.ROUTE_NAME = 'Princes Street'")


for row in c:
    #plot the searchpoint
    name1= row[0]
    r1 = row[1].read()
    ro1=r1[7:-1]
    ros1= ro1.split()
    
    folium.Marker(
            location =[float(ros1[1]), float(ros1[0])],
            icon = folium.DivIcon(
                icon_size=(150,36),
                icon_anchor=(7,29),
                html=f"""<div style="font-family: arial; color:orange"><b>{name1}</b>
<svg>
<circle cx="8" cy="8" r="6" fill="orange" opacity="1" />
</svg>
</div>""",
            )).add_to(mapp)


    #plot the route
    name3=row[3]
    r3 = row[4].read()
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


    #plot the point(s)
    r4 = row[2].read()
    ro4=r4[7:-1]
    ros4= ro4.split()
    folium.Marker(
            location =[float(ros4[1]), float(ros4[0])],
            icon = folium.Icon(color = 'blue', prefix='glyphicon', icon = 'question-sign')).add_to(mapp)


print("Content-type: text/html\n")
print(mapp.get_root().render())
