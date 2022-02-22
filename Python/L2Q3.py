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
#   Level 2  #
# Question 3 #
# Princess St#
##############

form=cgi.FieldStorage()
searchterm=form.getvalue('place')
query="select * from s1737656.points_game a, s1737656.searchpoints_game b where sp_id = 6 and sdo_nn(a.ora_geometry, b.ora_geometry, 'sdo_num_res=1') = 'TRUE'"


conn = cx_Oracle.connect(dsn="geoslearn",user="s2236682",password=pw)
c = conn.cursor()
c.execute(query)
html = ''
for row in c:
    if row[3] == '%s' %searchterm:
        
        print('<center><h1>Well Done! It\'s correct!</h1></center>')
        print('<center><img src=\"../../happy-dog.jpg\" style=\"width:auto;height:300px;\" alt=\"Happy Dog\"></center>')
        print(Markup('<br><br><b>Landmark: </b>'), row[3], Markup('<br><br><b>Landmark information: </b>'), row[6], Markup('<br><br><b>For more info: </b>'), row[5])
        print('<center><br><h2>Congratulations! You completed Level 2!</h2></center>')
        print('<center><br><br><button type=\"button" class=\"btn btn-info btn-lg\"><a href=\"https://www.geos.ed.ac.uk/~s2236682/asdm/L3Q1.html\">GO TO LEVEL 3</a></button></center>')
    else:
        print('<center><h3>Wrong Answer</h3></center>')
        print('<center><img src=\"../../sad-eyed-dog-with-book.jpg\" style=\"width:auto;height:300px;\" alt=\"Sad Dog\"></center>')
        print('<center><br> Go back and try again!</center>')
        print('<center><br><br><button type=\"button" class=\"btn btn-info btn-lg\"><a href=\"https://www.geos.ed.ac.uk/~s2236682/asdm/L2Q3.html\">Back</a></button></center>')

