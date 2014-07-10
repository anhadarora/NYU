# Gang Zhao, Assignment 2, Problem 3
class Borough:
    name = None
    zipcodes = None
    populations = 0
    popcount = 0
    incidents = 0

    def __init__(self, name):
        self.name = name
        self.zipcodes = []
        
    def addZipcode(self, zip):
        self.zipcodes.append(zip)

    def addPopulation(self, population):
        self.populations += population
        self.popcount += 1

    def addIncident(self, incident):
        self.incidents += incident
   
    
