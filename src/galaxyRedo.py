#!/usr/bin/python
##############################################>
##############################################>
##
##   Free BSD license 3-clause
##
##   Copyright (c)<2011>, <Martin de Bruyn>
##   All rights reserved.
##
##   Redistribution and use in source and binary forms, with or without
##   modification, are permitted provided that the following conditions are met:
##
##      - Redistributions of source code must retain the above copyright
##          notice, this list of conditions and the following disclaimer.
##      - Redistributions in binary form must reproduce the above copyright
##          notice, this list of conditions and the following disclaimer in the
##          documentation and/or other materials provided with the distribution.
##      - Neither the name of the <organization> nor the
##          names of its contributors may be used to endorse or promote products
##          derived from this software without specific prior written permission.
##
##   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
##   ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
##   WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
##   DISCLAIMED. IN NO EVENT SHALL <MARTIN DE BRUYN> BE LIABLE FOR ANY
##   DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
##   (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
##   LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
##   ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
##   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
##   SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
##
#########################################################################################>
#########################################################################################>

#  Developers.

#   MJ-meo-dmt.


####>   IMPORTS   <####

# System Imports.
import sys, os, random, math

# Panda Imports.

from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import *
from panda3d.core import NodePath
from direct.showbase.DirectObject import DirectObject

# Config (game).
from config import *

# Database Import.
from db import *

####>  CODE   <####

#           - MAIN-
####################>
base = ShowBase()   # FOR testing!! remove if done!

##############################
#     PATHS
##############################
# Create a var for dummySphere.
dummySphere = "../resources/models/planet_sphere"

##############################
#     NODES
##############################
## Setup Nodes ##
galaxyNode = render.attachNewNode("Galaxy")
sunNode = galaxyNode.attachNewNode("Sun")
mercuryNode = sunNode.attachNewNode("Mercury")
venusNode = sunNode.attachNewNode("Venus")
earthNode = sunNode.attachNewNode("Earth")
marsNode = sunNode.attachNewNode("Mars")
jupiterNode = sunNode.attachNewNode("Jupiter")
saturnNode = sunNode.attachNewNode("Saturn")
uranusNode = sunNode.attachNewNode("Uranus")
neptuneNode = sunNode.attachNewNode("Neptune")
plutoNode = sunNode.attachNewNode("Pluto")

###> Node setup END

##############################
#     DATABASE SETUPS
##############################
# Instance DataBase.
dataBase = db()
# Get the data from the sql_db and store it in a list.
planetData = []
planetData = dataBase.getPlanetDS(planetData)

# Get the sql data for each planet.
sunData = planetData[0]
mercuryData = planetData[1]
venusData = planetData[2]
earthData = planetData[3]
marsData = planetData[4]
jupiterData = planetData[5]
saturnData = planetData[6]
uranusData = planetData[7]
neptuneData = planetData[8]
plutoData = planetData[9]
###>

##############################
#     SKYBOX SETUP
##############################
base.setBackgroundColor(0,0,0,0) # Set the Background Color.

# Load the Skybox.
skyBox = loader.loadModel(SKYBOX_PATH)
skyBox.setBin("background", 1)
skyBox.setScale(1,1,1)
skyBox.setDepthTest(False)
skyBox.setZ(render, 0)
skyBox.setShaderOff()
skyBox.setLightOff()
skyBox.setCompass()
skyBox.reparentTo(base.camera)
print "SkyBox Loaded..."
###>

# This should move!
base.camLens.setFov(camFov)
base.camLens.setNear(camNear)
base.camLens.setFar(camFar)
        
##############################
#     CLASSES - SYSTEMs &  PLANETS
##############################
# The New classes.
# This class controls the systems.
# And stores planets e.g.
class PlanetSystem:
    def __init__(self, systemName):
        # Lets name the system.
        self.systemName = systemName
        
        # Empty place for stars. like the 'Sun'
        self.stars = {}
        
        # Empty Dict. for planets.
        self.planets = {}
        
        # Empty Dict. for the moons. for the many :P
        self.moons = {}
        
        # Empty Dict. for dwarf stars.
        self.dwarf = {}
        
    # Methods for adding planets to the Dict.
    def addStars(self, starsName, starsInstance):
        self.stars[starsName] = starsInstance
    
    def addPlanet(self, planetName, planetInstance):
        self.planets[planetName] = planetInstance
        
    def addDwarf(self, dwarfName, dwarfInstance):
        self.dwarf[dwarfName] = dwarfInstance
        
    # Method for adding moons.
    def addMoons(self, moonsName, moonsInstance):
        self.moons[moonName] = moonInstance
###> PlanetSystem Class END.


# Creating planets. Feed the data to make planets... :)
class Planet:
    def __init__(self, name, modelPath, planetNode, planetPos, planetScale, planetType="Terrestrial"):
        # Add a name to the planet
        self.name = name
        
        # Add a model to the planet.
        self.np = loader.loadModel(modelPath)
        
        # Render it, set it, size it... 
        self.np.reparentTo(planetNode)
        self.np.setPos(planetPos)
        self.np.setScale(planetScale)
        
        # Give it a type, "Terrestrial" = "rock, metal" other "Jovian" = "hydrogen, helium"
        self.planetType = planetType

        # Print out Confirm.
        print "Planet: %s with Type: %s - Created..." % (name, planetType)
###> Planet Class END.


# This class creates moons.
class Moon:
    def __init__(self, name, moonType="rock"):
        # Give the moon a name.
        self.name = name
        # Add a type to the moon.
        self.moonType = moonType
        print "Moon: %s with Type: %s - Created..." % (name, moonType)
###> Moon Class END.

##############################
#            LIGHTS 
##############################

# Setup basic lights.
# Ambient Lights.
baseAmbientLight = AmbientLight('AmbientLight')
baseAmbientLight.setColor(VBase4(0.1, 0.1, 0.1, 1))
baseAmbientLightNode = render.attachNewNode(baseAmbientLight)
render.setLight(baseAmbientLightNode)
###>
    
# Setup Point Light for "Star/Sun".
sunLight = PointLight('sunLight')
sunLight.setColor(VBase4(3, 3, 3, 1))
#sunLight.setSpecularColor(VBase4(1, 1, 1, 1))
sunLightNode = galaxyNode.attachNewNode(sunLight)
sunLightNode.setPos(0, 0, 0)
render.setLight(sunLightNode)
###>

##############################
#     INSTANCE SYSTEM & PLANETS
##############################
galaxy = PlanetSystem("System 1")

### Instance planets ###
# theplanet = Planet(name, planetType="rock") \\ Have to figure out how to make use of setPos within class... Noob :P
# Check the planet types...

# Sun (star).
sun = Planet("Sun", dummySphere, sunNode, sunData[0], sunData[1], "Star")
galaxy.addStars("Sun", sun)
# Mercury
mercury = Planet("Mercury", dummySphere, mercuryNode, mercuryData[0], mercuryData[1])
galaxy.addPlanet("Mercury", mercury)
# Venus
venus = Planet("Venus", dummySphere, venusNode, venusData[0], venusData[1])
galaxy.addPlanet("Venus", venus)
# Earth
earth = Planet("Earth", dummySphere, earthNode, earthData[0], earthData[1])
galaxy.addPlanet("Earth", earth)
# Mars
mars = Planet("Mars", dummySphere, marsNode, marsData[0], marsData[1])
galaxy.addPlanet("Mars", mars)
# Jupiter
jupiter = Planet("Jupiter", dummySphere, jupiterNode, jupiterData[0], jupiterData[1], "Jovian")
galaxy.addPlanet("Jupiter", jupiter)
# Saturn
saturn = Planet("Saturn", dummySphere, saturnNode, saturnData[0], saturnData[1], "Jovian")
galaxy.addPlanet("Saturn", saturn)
# Uranus
uranus = Planet("Uranus", dummySphere, uranusNode, uranusData[0], uranusData[1], "Jovian")
galaxy.addPlanet("Uranus", uranus)
# Neptune
neptune = Planet("Neptune", dummySphere, neptuneNode, neptuneData[0], neptuneData[1], "Jovian")
galaxy.addPlanet("Neptune", neptune)
# Pluto
pluto = Planet("Pluto", dummySphere, plutoNode, plutoData[0], plutoData[1], "Dwarf Planet")
galaxy.addPlanet("Pluto", pluto)

###> Instance END

print render.ls()
run()








