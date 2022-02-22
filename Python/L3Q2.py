#!/usr/bin/env python3
import cx_Oracle
import cgi
import cgitb
from markupsafe import Markup
from jinja2 import Environment, FileSystemLoader
cgitb.enable()

with open("../../../nada",'r') as pwf:
    pw = pwf.read().strip()

print("Content-Type: text/html\n")
print("<!DOCTYPE html>")
print("<head>")
print("<style>")
print("table,th,td{border:1px solid black;}")
print("</style>")
print("</head>")
print("<body>")

form=cgi.FieldStorage()
searchterm=form.getvalue('place')
query="SELECT * FROM s1737656.SEARCHPOINTS_GAME A, s1737656.POLYGONS_GAME B WHERE SDO_NN(B.ORA_GEOMETRY, A.ORA_GEOMETRY, 'sdo_num_res=2') = 'TRUE' AND A.SP_ID = '9' and b.poly_id != '20'"

#############
#We used the below query to find the name and ID of the nearest polygon.
#And we set the 'sdo_num_res=2 to return two results
#And we set the query not equal to the nearest

#SQL> SELECT poly_name, poly_id FROM s1737656.SEARCHPOINTS_GAME A, s1737656.POLYGONS_GAME B WHERE SDO_NN(B.ORA_GEOMETRY, A.ORA_GEOMETRY, 'sdo_num_res=1') = 'TRUE' AND A.SP_ID = '9';
##############

conn = cx_Oracle.connect(dsn="geoslearn",user="s2236682",password=pw)
c = conn.cursor()
c.execute(query)
html = ''
for row in c:
    if row[9] == '%s' %searchterm:
        
        print('<center><h1>Well Done! It\'s correct!</h1></center>')
        print('<center><img src=\"../../happy-dog.jpg\" style=\"width:auto;height:300px;\" alt=\"Happy Dog\"></center>')
        print(Markup('<br><br><b>Landmark: </b>'), row[9])
        print('<center><br><br><button type=\"button" class=\"btn btn-info btn-lg\"><a href=\"https://www.geos.ed.ac.uk/~s2236682/asdm/L3Q3.html\">NEXT QUESTION</a></button></center>')
    else:
        print('<center><h3>Wrong Answer</h3></center>')
        print('<center><img src=\"../../sad-eyed-dog-with-book.jpg\" style=\"width:auto;height:300px;\" alt=\"Sad Dog\"></center>')
        print('<center><br> Go back and try again!</center>')
        print('<center><br><br><button type=\"button" class=\"btn btn-info btn-lg\"><a href=\"https://www.geos.ed.ac.uk/~s2236682/asdm/L3Q2.html\">Back</a></button></center>')

