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
# If skybox changes.. we can change it in config.
pathBox = skyboxPath
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
        
        # Empty Dict. for planets.
        self.planets = {}
        
        # Empty Dict. for the moons.
        self.moons = {}
        
    # Method for adding planets to the Dict.
    def addPlanet(self, planetName, planetInstance):
        self.planets[planetName] = planetInstance
    
    # Method for adding moons.
    def addMoon(self, moonName, moonInstance):
        self.moons[moonName] = moonInstance
###> PlanetSystem Class END.


# This class creates new planets.
class Planet():
    def __init__(self, name, planetType="rock"):
        # Add a name to the planet
        self.name = name
        # Add a type to the planet.
        self.planetType = planetType
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
baseAmbientLight.setColor(VBase4(0, 0, 0, 1))
baseAmbientLightNode = render.attachNewNode(baseAmbientLight)
render.setLight(baseAmbientLightNode)
###>
    
# Setup Point Light for "Star/Sun".
sunLight = PointLight('sunLight')
sunLight.setColor(VBase4(3, 3, 3, 1))
#sunLight.setSpecularColor(VBase4(1, 1, 1, 1))
sunLightNode = galaxyNode.attachNewNode(sunLight)
sunLightNode.setPos(0, 0, 0)
sunLightNode.setScale(10)
render.setLight(sunLightNode)
###>

##############################
#     INSTANCE SYSTEM & PLANETS
##############################
galaxy = PlanetSystem("System 1")

### Instance planets ###
# theplanet = Planet(name, planetType="rock") \\ Have to figure out how to make use of setPos within class... Noob :P
# Sun
sun = Planet("Sun", "Gas")
galaxy.addPlanet("Sun", sun)
# Mercury
mercury = Planet("Mercury")
galaxy.addPlanet("Mercury", mercury)
# Venus
venus = Planet("Venus")
galaxy.addPlanet("Venus", venus)
# Earth
earth = Planet("Earth", "Ice")
galaxy.addPlanet("Earth", earth)
# Mars
mars = Planet("Mars", "Desert")
galaxy.addPlanet("Mars", mars)
# Jupiter
jupiter = Planet("Jupiter", "Gas")
galaxy.addPlanet("Jupiter", jupiter)
# Saturn
saturn = Planet("Saturn")
galaxy.addPlanet("Saturn", saturn)
# Uranus
uranus = Planet("Uranus")
galaxy.addPlanet("Uranus", uranus)
# Neptune
neptune = Planet("Neptune", "Water")
galaxy.addPlanet("Neptune", neptune)
# Pluto
pluto = Planet("Pluto", "Ice")
galaxy.addPlanet("Pluto", pluto)

###> Instance END

##################################
#    SETUP PLANET LOC, SCALE...
##################################
# Testing material for sun.
sunMat = Material()
sunMat.setShininess(3.0)
sunMat.setDiffuse(VBase4(254, 157, 58, 1))
sunMat.setAmbient(VBase4(254, 157, 58, 1))
sunMat.setEmission(VBase4(0.6, 0.6, 0, 1))
sunMat.setSpecular(VBase4(254, 157, 58, 1))
#sunMat.setTwoside(True)


### SETUP PLANETS ###

# Starting with the sun.
galaxy.planets['Sun'] = loader.loadModel(dummySphere)
galaxy.planets['Sun'].reparentTo(sunNode)
galaxy.planets['Sun'].setMaterial(sunMat)
galaxy.planets['Sun'].setPos(0, 0, 0)
galaxy.planets['Sun'].setScale(sunData[1])

galaxy.planets['Mercury'] = loader.loadModel(dummySphere)
galaxy.planets['Mercury'].reparentTo(mercuryNode)
galaxy.planets['Mercury'].setPos(1, 0, 0)
galaxy.planets['Mercury'].setScale(mercuryData[1])

galaxy.planets['Venus'] = loader.loadModel(dummySphere)
galaxy.planets['Venus'].reparentTo(venusNode)
galaxy.planets['Venus'].setPos(2, 0, 0)
galaxy.planets['Venus'].setScale(venusData[1])

galaxy.planets['Earth'] = loader.loadModel(dummySphere)
galaxy.planets['Earth'].reparentTo(earthNode)
galaxy.planets['Earth'].setPos(3, 0, 0)
galaxy.planets['Earth'].setScale(earthData[1])

galaxy.planets['Mars'] = loader.loadModel(dummySphere)
galaxy.planets['Mars'].reparentTo(marsNode)
galaxy.planets['Mars'].setPos(4, 0, 0)
galaxy.planets['Mars'].setScale(marsData[1])

galaxy.planets['Jupiter'] = loader.loadModel(dummySphere)
galaxy.planets['Jupiter'].reparentTo(jupiterNode)
galaxy.planets['Jupiter'].setPos(5, 0, 0)
galaxy.planets['Jupiter'].setScale(jupiterData[1])

galaxy.planets['Saturn'] = loader.loadModel(dummySphere)
galaxy.planets['Saturn'].reparentTo(saturnNode)
galaxy.planets['Saturn'].setPos(6, 0, 0)
galaxy.planets['Saturn'].setScale(saturnData[1])

galaxy.planets['Uranus'] = loader.loadModel(dummySphere)
galaxy.planets['Uranus'].reparentTo(uranusNode)
galaxy.planets['Uranus'].setPos(7, 0, 0)
galaxy.planets['Uranus'].setScale(uranusData[1])

galaxy.planets['Neptune'] = loader.loadModel(dummySphere)
galaxy.planets['Neptune'].reparentTo(neptuneNode)
galaxy.planets['Neptune'].setPos(8, 0, 0)
galaxy.planets['Neptune'].setScale(neptuneData[1])

galaxy.planets['Pluto'] = loader.loadModel(dummySphere)
galaxy.planets['Pluto'].reparentTo(plutoNode)
galaxy.planets['Pluto'].setPos(9, 0, 0)
galaxy.planets['Pluto'].setScale(plutoData[1])

print render.ls()
run()








