# Gang Zhao, Assignment 4, Problem 1, 11/2/2013
import MySQLdb
import csv
# Connect MySQL
db = MySQLdb.connect(host = "localhost",
                   user = "gz475",
                   passwd = "123456",
                   db = "coursedb")
cur = db.cursor()
# Drop duplicate tables 
cur.execute("DROP TABLE IF EXISTS boroughs")
cur.execute("DROP TABLE IF EXISTS zipcodes")
cur.execute("DROP TABLE IF EXISTS incidents")
# Create three tables
createCommand = "create table boroughs (zipcode varchar(255), boroughname varchar(255), primary key(zipcode))"
cur.execute(createCommand)              
createCommand = "create table zipcodes (zipcode varchar(255), area decimal(21,20), population int)"
cur.execute(createCommand)              
createCommand = "create table incidents (incidentaddress varchar(255), zipcode varchar(255) , uniquekey int)"
cur.execute(createCommand)
# Read data from borough file and insert into boroughs table
boroughfile = open('boroughs.csv','r')
boroughcon = csv.reader(boroughfile,delimiter= ',')
for x in boroughcon:
    zipcode = x[0]
    borough = x[1]
    insertCommand = "insert into boroughs values("+"'"+str(zipcode)+"'"+","+"'"+str(borough)+"'"+")"+"ON DUPLICATE KEY UPDATE" + " zipcode = " + zipcode + ";" #Make sure there're no duplicate records in boroughs
    cur.execute(insertCommand)
# Read data from zipCode file and insert into zipcodes table
zipcodesfile = open('zipCodes.csv','r')
zipcodescon = csv.reader(zipcodesfile,delimiter= ',')
num = 0
for x in zipcodescon:
    if num == 0:
        num += 1
        continue
    else:
        zipcode = x[0]
        area = x[7]
        popu = x[10]
        if popu != '':
            insertCommand = "insert into zipCodes values("+"'"+str(zipcode)+"'"+","+str(area)+","+str(popu)+");"
            cur.execute(insertCommand)
# Read data from incident file and insert into incidents table
incidentsfile = open('Incidents_grouped_by_Address_and_Zip.csv','r')
incidentscon = csv.reader(incidentsfile,delimiter= ',')
num = 0
for x in incidentscon:
    if num == 0:
        num += 1
        continue
    else:
        address = x[0]
        zipcode = x[1]
        count = x[2]
        if (zipcode.isdigit()):
            address = address.replace("'","")# deal with "'" in addresses
            insertCommand = "insert into incidents values("+"'"+str(address)+"'"+","+"'"+str(zipcode)+"'"+","+str(count)+");"
            cur.execute(insertCommand) 
db.commit()
db.close()
