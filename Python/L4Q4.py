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

##############
#   Level 4  #
# Question 4 #
#Stockbridge #
##############

form=cgi.FieldStorage()
searchterm=form.getvalue('place')
query="SELECT A.POLY_ID, A.POLY_NAME, SDO_GEOM.SDO_AREA(A.ORA_GEOMETRY, 0.005) FROM s1737656.POLYGONS_GAME A, s1737656.SEARCHPOL_GAME B WHERE SDO_RELATE(A.ORA_GEOMETRY, B.ORA_GEOMETRY, 'MASK=ANYINTERACT QUERYTYPE=WINDOW') = 'TRUE' AND SPOL_ID = '0' AND POLY_ID = '6'"


conn = cx_Oracle.connect(dsn="geoslearn",user="s2236682",password=pw)
c = conn.cursor()
c.execute(query)
html = ''
for row in c:
    if row[1] == '%s' %searchterm:
        
        print('<center><h1>Well Done! It\'s correct!</h1></center>')
        print('<center><img src=\"../../happy-dog.jpg\" style=\"width:auto;height:300px;\" alt=\"Happy Dog\"></center>')
        print(Markup('<br><br><b>Landmark: </b>'), row[1], Markup('<br><br><b>The correct area of the Royal Botanic Gardens is: </b>'), row[2])
        print('<center><br><h2>Congratulations! You completed the game!</h2></center>')
        print('<center><br><h2>Your prize is a private dinner with Bruce!</h2></center>')
        print('<center><br><br><button type=\"button" class=\"btn btn-info btn-lg\"><a href=\"https://www.geos.ed.ac.uk/~s2236682/asdm/GuessED.html\">BACK TO THE HOME PAGE</a></button></center>')
    else:
        print('<center><h3>Wrong Answer</h3></center>')
        print('<center><img src=\"../../sad-eyed-dog-with-book.jpg\" style=\"width:auto;height:300px;\" alt=\"Sad Dog\"></center>')
        print('<center><br> Go back and try again!</center>')
        print('<center><br><br><button type=\"button" class=\"btn btn-info btn-lg\"><a href=\"https://www.geos.ed.ac.uk/~s2236682/asdm/L4Q3.html\">Back</a></button></center>')

