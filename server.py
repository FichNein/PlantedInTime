from flask import Flask, escape, request, render_template, url_for
import os, os.path

# ----- SERVER ----- #

SPECIESLOC = "./static/species"
SPECIESLIST = []


def growSpecies():
    allSpecies = os.listdir(SPECIESLOC)
    
    for species in allSpecies:
        path = SPECIESLOC + "/" + species
        SPECIESLIST.append(Species(path))
        
            


def growPlants(species):
    if type(species) is list:
        for specie in species:
            plants = os.listdir(specie.path)
            for plant in plants:
                if plant != "species.txt":
                    specie.add(Plant(specie, specie.path + "/" + plant))
    
    elif type(species) is Species:
        plants = os.listdir(species.path)
        for plant in plants:
                if plant != "species.txt":
                    specie.add(Plant(specie, specie.path + "/" + plant))


class Plant:

    def __init__(self, parent, path):
        self.path = path
        self.staticPath = path[9:]
        self.parent = parent
        try:
            with open(path + "/info.txt", 'r') as file:
                lines = file.readlines()
                self.count = len(os.listdir(path + '/photos'))
                self.start = (lines[1][3:]).strip()
                self.end = (lines[2][3:]).strip()
        except:
            print("Failed to open Plant Info")



class Species:

    def __init__(self, path):
        self.path  = path
        self.staticPath = path.strip('./static/')
        self.plants = []
        try:
            with open(path + "/species.txt", 'r') as file:
                lines = file.readlines()
                self.name = (lines[0][3:]).strip()
                self.latin = (lines[1][3:]).strip()
        except:
            print("Failed to Open Species Info")

    def add(self, plant):
        self.plants.append(plant)

    # ---- Debug Prints ---- #

    def printPlants(self):
        for plant in self.plants:
            print(self.name + ",", self.latin + ": ", end="")
            plant.print()

    # ---- Front End Requests ---- #

    def getSelf(self):
        return self.name + ",", self.latin

    def getPlants(self):
        for plant in self.plants:
            print(self.name + ",", self.latin + ": ", end="")
            plant.print()

    def getPlant(self, start):
        for plant in self.plants:
            if plant.start == start:
                return plant

        return None

def findSpecies(name):
    for species in SPECIESLIST:
        if species.name == name:
            return species
    
    return "Plant Not Found"

def getPhotoPath(plant):
    return plant.staticPath + '/photos/' + str(1) + '.jpg'

"""
if __name__ == "__main__":
    growSpecies()
    growPlants(SPECIESLIST)
    for spec in SPECIESLIST:
        spec.printPlants()
"""    


# ----- FLASK ----- #

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    return render_template("home.html", species=SPECIESLIST, len=len(SPECIESLIST))


@app.route('/<string:species>')
def speciesRespone(species):
    species = findSpecies(species)
    return render_template("species.html", specie=species.name , plants=species.plants, len=len(species.plants))

@app.route('/<string:species>/<string:start>')
def plantResponse(species, start):
    species = findSpecies(species)
    plant = species.getPlant(start)
    finalPath = getPhotoPath(plant)
    return render_template("plant.html", finalPhotoPath=finalPath, count=plant.count, specie=species.name, start=plant.start, end=plant.end)


growSpecies()
growPlants(SPECIESLIST)

if __name__ == "__main__":
    #app.run(debug=True)
    app.run()

