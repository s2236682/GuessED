#!/usr/bin/env python3
import cgi
import cgitb
import folium
import numpy as np
import cx_Oracle

cgitb.enable()

with open("../../nadaa",'r') as pwf:
    pw = pwf.read().strip()


mapp = folium.Map(location=[55.952867,-3.172500], max_zoom=20, zoom_start=18, tiles='cartodbdark_matter')
folium.TileLayer('openstreetmap', name ='I need help').add_to(mapp)
folium.LayerControl().add_to(mapp)

conn = cx_Oracle.connect(dsn="geoslearn",user="s1737656",password=pw)
c = conn.cursor()

c.execute("SELECT A.SP_NAME, SDO_UTIL.TO_WKTGEOMETRY(A.ORA_GEOMETRY), B.POLY_NAME, SDO_UTIL.TO_WKTGEOMETRY(B.ORA_GEOMETRY), C.ROUTE_NAME, SDO_UTIL.TO_WKTGEOMETRY(C.ORA_GEOMETRY) FROM SEARCHPOINTS_GAME A, POLYGONS_GAME B, ROUTES_GAME C WHERE A.SP_NAME = 'C' AND B.POLY_NAME = 'Holyrood Palace' AND C.ROUTE_NAME = 'Royal Mile'")


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
            

    #plot the polygon(s)
    name2 = row[2]
    r2 = row[3].read()
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
    
    folium.vector_layers.Polygon(locarray2, popup=name2).add_to(mapp)

    #plot the route
    name3=row[4]
    r3 = row[5].read()
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

    """
    #plot the point(s)
    r4 = row[6].read()
    ro4=r4[7:-1]
    ros4= ro4.split()
    folium.Marker(
            location =[float(ros4[1]), float(ros4[0])],
            icon = folium.Icon(color = 'blue', prefix='glyphicon', icon = 'question-sign')).add_to(mapp)


    #name= row[5]
    r4 = row[5].read()
    ro4 = r4[10:-2]
    ros4 = ro4.split(",")

    location4 = []
    for i in ros4:
        l4= i.split()
        location4.append((float(l4[1]), float(l4[0])))
        
    locarray4= []
    for j in location4:
        lista4=[*j]
        locarray4.append(lista4)

    folium.vector_layers.Polygon(locarray4).add_to(mapp)


 

    def iconcolor(inname):
        if row[3] == 1:
            iconn = folium.Icon('green')

        else:
            iconn = folium.Icon('red')
        return iconn
        
    Marker1 = folium.Marker(
            location =[float(ros1[1]), float(ros1[0])],
            popup = name1,
            icon = iconcolor(l)).add_to(mapp)
 
    if row[0] == 1:
        #folium.Marker(row[1:],popup=row[0]).add_to(mapp) -- ORIGINAL (PRAC 7)
    
        #WKT TEST
        #iconurl1="https://www.geos.ed.ac.uk/~s1737656/ASDM/images/Aqua.png"
        #icon1 = folium.features.CustomIcon(iconurl1)
        name1= row[1]
        r1 = row[2].read()
        ro1=r1[7:-1]
        ros1= ro1.split()
        Marker1 = folium.Marker(
            location =[float(ros1[1]), float(ros1[0])],
            popup = name1)
            #icon = folium.Icon(color='red')).add_to(mapp)
            #icon=folium.DivIcon({name1}).add_to(mapp)
    else:
         name2 = row[1]
         r2 = row[2].read()
         ro2=r2[7:-1]
         ros2= ro2.split()
         Marker2 =folium.Marker(location =[float(ros2[1]), float(ros2[0])],
                      popup=name2,
                      icon = folium.Icon(color='red', icon='none')).add_to(mapp)

    #Marker1.add_to(mapp)
    #Marker2.add_to(mapp)
    
   

    GEOJSON TEST
    r= row[0].read()[2:-3]
    #cc= r.strip()[1:-1].split(",")
    #print(cc)
    coords = r[34:71].split(", ")
    #print(coords)
    scoords = []
    for i in coords:
        scoords.append(float(i))
            
    print(scoords)
    """


 
#WKT - WITH WKT PACKAGE TO CONVERT TO GEOJSON
#for row in c:
    #row_json = wkt.loads(' '.join(map(str, row)))
    #print(row_json)
    #geojson_layer=folium.GeoJson(row_json)
    #geojson_layer.add_to(mapp)


#c.close()

print("Content-type: text/html\n")
print(mapp.get_root().render())
