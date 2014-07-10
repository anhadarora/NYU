# Gang Zhao, Assignment4, Problem 3
import MySQLdb
import sys
# Connect to the database
db = MySQLdb.connect(host = "localhost",
                   user = "gz475",
                   passwd = "123456",
                   db = "coursedb")
cur = db.cursor()
# Get borough name
boroughname = sys.argv[1]
# Caculate the total population of the given borough
query = "select sum(population) from zipcodes Z where Z.zipcode in (select B.zipcode from boroughs B where B.boroughname = " + "'" +boroughname + "'" + "); "
cur.execute(query)
population = cur.fetchall()
if population[0][0] is None:
    print 'None'
    sys.exit(0)
totalpop = population[0][0]
# Caculate the total incidnets of the given borough
query = "select sum(uniquekey) from incidents I where I.zipcode in (select B.zipcode from boroughs B where B.boroughname = " + "'" +boroughname + "'" + "); "
cur.execute(query)
incidents = cur.fetchall()
totalincid = incidents[0][0]
# Output
print float(totalincid)/float(totalpop)
