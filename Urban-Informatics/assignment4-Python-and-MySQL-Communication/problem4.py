# Gang Zhao, Assignment4, Problem 4
import MySQLdb
import sys
# Connect to the database
db = MySQLdb.connect(host = "localhost",
                   user = "gz475",
                   passwd = "123456",
                   db = "coursedb")
cur = db.cursor()
# Find out incidents in Manhattan
query = "select incidentaddress from incidents I where I.zipcode in (select B.zipcode from boroughs B where B.boroughname = 'Manhattan'); "
cur.execute(query)
address = cur.fetchall()
# Print the addresses
for x in range(0, len(address)):
    if address[x][0] != '':# The addresses without specific details are not printed
        print address[x][0]
