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

###########
#Change it to buffer!

form=cgi.FieldStorage()
searchterm=form.getvalue('place')
query="SELECT * FROM s1737656.POLYGONS_GAME A, s1737656.SEARCHPOINTS_GAME B WHERE SDO_NN(A.ORA_GEOMETRY, B.ORA_GEOMETRY, 'sdo_num_res=1') = 'TRUE' AND B.SP_NAME = 'D' AND B.SP_LVL = '2'"

conn = cx_Oracle.connect(dsn="geoslearn",user="s2236682",password=pw)
c = conn.cursor()
c.execute(query)
html = ''
for row in c:
    if row[4] == '%s' %searchterm:
        print('<center><h1>Well Done! It\'s correct!</h1></center>')
        print('<center><img src=\"../../happy-dog.jpg\" style=\"width:auto;height:300px;\" alt=\"Happy Dog\"></center>')
        print(Markup('<br><br><b>Landmark: </b>'), row[4], Markup('<br><br><b>Landmark information: </b>'), row[5], Markup('<br><br><b>For more info: </b>'), row[6])
        print('<center><br><br><button type=\"button" class=\"btn btn-info btn-lg\"><a href=\"https://www.geos.ed.ac.uk/~s2236682/asdm/L2Q2.html\">NEXT QUESTION</a></button></center>')
    else:
        print('<center><h3>Wrong Answer</h3></center>')
        print('<center><img src=\"../../sad-eyed-dog-with-book.jpg\" style=\"width:auto;height:300px;\" alt=\"Sad Dog\"></center>')
        print('<center><br> Go back and try again!</center>')
        print('<center><br><br><button type=\"button" class=\"btn btn-info btn-lg\"><a href=\"https://www.geos.ed.ac.uk/~s2236682/asdm/L2Q1.html\">Back</a></button></center>')

