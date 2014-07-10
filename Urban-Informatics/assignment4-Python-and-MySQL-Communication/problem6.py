# Gang Zhao, Assignment4, Problem 6
import MySQLdb
import sys
# Connect to the database
db = MySQLdb.connect(host = "localhost",
                   user = "gz475",
                   passwd = "123456",
                   db = "coursedb")
cur = db.cursor()
# Find the incients in Manhattan and their zipcodes and populations
query = "select B.zipcode, Z.population  from boroughs B, zipcodes Z where B.zipcode = Z.zipcode and B.boroughname = 'Manhattan' and B.zipcode in (select I.zipcode from incidents I); "
cur.execute(query)
zipandpop = cur.fetchall()
# Output zipcodes and populations
for x in range(0, len(zipandpop)):
    print zipandpop[x][0],zipandpop[x][1]
