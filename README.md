# GuessED :mag:

An Edinburgh-based landmark guessing game aimed at locals and non-locals alike.

Click [here](https://www.geos.ed.ac.uk/~s2236682/asdm/GuessED.html) to access the game.

## Introduction

We created a database-driven guessing game that is based in Edinburgh using spatial queries. 

## Methodology
Our group took advantage of the capabilities offered by Oracle Spatial and integrated the database using the cx_Oracle Python extension module. Selected Edinburgh landmarks were digitised as points, polylines or polygons in QGIS and imported into Oracle using the OGR2OGR command line tool in in theOSGeo4W shell as shown below:

```sql
ogr2ogr -overwrite -f OCI OCI:<username>/<password>@database "C:\Workspace\Example.shp" -t_srs "EPSG:4326" -nln <TABLE NAME>
```

In the guessing component of the game, users are presented with a question, a map inset, a series of radio buttons from which to pick what they believe is the correct answer and, lastly, a hint on how to answer the question. Upon clicking on the “submit” button, a Python script runs, using Python extension module cx_Oracle to query our database.

## Database
### Data model
Our group took advantage of the capabilities offered by Oracle Spatial. 

GuessED’s data model comprises of 5 tables as seen below:

![Data Model](Images/datamodel.jpg "Data Model") 

OGR2OGR automatically assigns a primary key (OGR_FID) to each table and saves the geometry as “ORA_GEOMETRY”. Furthermore, OGR automatically creates a metadata table and assigns a spatial index to objects in the ORA_GEOMETRY. [Learn more](https://gdal.org/drivers/vector/oci.html)

### Oracle Spatial
14 key landmarks were identified for querying. Accordingly, 14 different queries were designed to return each of them as the only possible answer. A few different query types were used to maximise the use of Oracle Spatial operators.



## Project Team
**Team Leader:** Denise

**SQL Officer:** Daiqiao

**Python Officer:** Attila

## 
A group project for the Advanced Spatial Database Methods module at the University of Edinburgh.
