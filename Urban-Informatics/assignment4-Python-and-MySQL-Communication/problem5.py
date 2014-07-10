# Gang Zhao, Assignment4, Problem 5
import MySQLdb
import sys
# Connect to the database
db = MySQLdb.connect(host = "localhost",
                   user = "gz475",
                   passwd = "123456",
                   db = "coursedb")
cur = db.cursor()
# Find the incients in Bronx or Queens
query = "select incidentaddress from incidents I where I.zipcode in (select B.zipcode from boroughs B where B.boroughname = 'Bronx' or B.boroughname = 'Queens'); "
cur.execute(query)
address = cur.fetchall()
# Output addresses
for x in range(0, len(address)):
    if address[x][0] != '':# The incidents without specific details are not printed
        print address[x][0]
