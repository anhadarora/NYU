# Gang Zhao, Assignment 4, Problem2
import MySQLdb
import sys
# Catch input
code = sys.argv[1]
# Connect MySQL
db = MySQLdb.connect(host = "localhost",
                   user = "gz475",
                   passwd = "123456",
                   db = "coursedb")
cur = db.cursor()
# Find out the population and area of given zipcode
query = "select population from zipcodes where zipcode = " + "'" + code + "'"+ ";"
cur.execute(query)
population = cur.fetchall()
query = "select area from zipcodes where zipcode = " + "'" + code + "'"+ ";"
cur.execute(query)
area = cur.fetchall()
# No record in zipcodes print None
if len(population)==0:
    print 'None'
# One and multi records output
if len(population)>= 1:
    for x in range(0,len(population)):# If one zipcode has more than one record, cacalate the density of records separately
        print float(population[x][0])/float(area[x][0])

