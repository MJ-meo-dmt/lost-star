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

#from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import *
from direct.showbase.DirectObject import DirectObject

# Config (game).
from config import *

# Database Import.
from db import *

####>  CODE   <####

# Galaxy Class - MAIN-
####################>
class Galaxy(DirectObject):
    
    # ShowBase.
    def __init__(self):
        #ShowBase.__init__(self)
        
        print "Starting Galaxy..."
        base.setBackgroundColor(0,0,0,0)
        
        # Load the Skybox.
        self.skyBox = loader.loadModel("../resources/models/Skybox.egg")#("skyBoxNew.egg")#
        self.skyBox.setBin("background", 0)
        self.skyBox.setScale(1,1,1)
        self.skyBox.setDepthTest(False)
        self.skyBox.setZ(render, 0)
        self.skyBox.clearLight()
        self.skyBox.setCompass()
        self.skyBox.reparentTo(base.camera)
        
        print "SkyBox Loaded..."
        ###>
        
        base.camLens.setFov(camFov)
        base.camLens.setNear(camNear)
        base.camLens.setFar(camFar)
        
        # Setup basic lights.
        # Ambient Lights.
        self.baseAmbientLight = AmbientLight('baseAmbientLight')
        self.baseAmbientLight.setColor(VBase4(0.1, 0.1, 0.1, 1))
        self.baseAmbientLightNode = render.attachNewNode(self.baseAmbientLight)
        render.setLight(self.baseAmbientLightNode)
        ###>
    
        # Setup Point Light for "Star/Sun".
        self.sunLight = PointLight('sunLight')
        self.sunLight.setColor(VBase4(0.6, 0.6, 0.6, 1))
        self.sunLightNode = render.attachNewNode(self.sunLight)
        self.sunLightNode.setPos(0, 0, 0)
        render.setLight(self.sunLightNode)
        ###>
        
        #  LOAD SYSTEM.
        Galaxysystem = System1()
    
    # GALAXY END.

# System Class. -SUB-
class System1():
    
    def __init__(self):
        
        # Create System Dummy nodes.
        self.system1Node = render.attachNewNode('system 1')
        print self.system1Node
        
        # DB Instance.
        # So we can get data from 'planetData' table.
        DB = db()
        self.planets(DB)
        
        # Galaxy Instance.
        #initGalaxy = Galaxy()
        #self.sunlight = initGalaxy.sunlight()
        #render.setLight(self.sunlight)
        
        
    def planets(self, DB):
        
        # Set the variables for scale and distance changes; (like global var)
        orbitDis = 30 # This is the 30cm from the model. (From the scale pdf, ask me)
        sunHalf = 1.5 # This is sunScale / 2 and cheated to fit in with rest of the scale/slash/Distance (needs work!)
        
        # Creating Dummy nodes for stars/planets.
        self.sunNode = self.system1Node.attachNewNode('Sun')
        self.planet1Node = self.sunNode.attachNewNode('Planet1')
        self.planet2Node = self.sunNode.attachNewNode('Planet2')
        self.planet3Node = self.sunNode.attachNewNode('Planet3')
        self.planet4Node = self.sunNode.attachNewNode('Planet4')
        self.planet5Node = self.sunNode.attachNewNode('Planet5')
        self.planet6Node = self.sunNode.attachNewNode('Planet6')
        self.planet7Node = self.sunNode.attachNewNode('Planet7')
        self.planet8Node = self.sunNode.attachNewNode('Planet8')
        self.planet9Node = self.sunNode.attachNewNode('Planet9')
        
        print self.system1Node.ls()
        
        # Get data from sql_db.
        # Make a list to hold the 'planetData'
        planetData = []
        planetData = DB.getPlanetDS(planetData)
        
        # Assign sql data to a planet'Data' var.
        # So we can slice it for 'planetDis' and 'planetScale'
        # planetData[0-9] = planetID from sql-db.
        sunData = planetData[0]
        planet1Data = planetData[1]
        planet2Data = planetData[2]
        planet3Data = planetData[3]
        planet4Data = planetData[4]
        planet5Data = planetData[5]
        planet6Data = planetData[6]
        planet7Data = planetData[7]
        planet8Data = planetData[8]
        planet9Data = planetData[9]
        
        # To use or get data:  use planet(1-9)Data[0-1].  0 = planetDistance. 1 = planetScale.
        # print planet9Data[0]
        # print planet9Data[1]
        
        # Create a var for dummySphere.
        dummySphere = "../resources/models/planet_sphere"
        
        # In order from 'planetID', load the planets.
        
        # Testing material for sun.
        sunMat = Material()
        sunMat.setShininess(1.0)
        sunMat.setDiffuse(VBase4(1, 1, 0, 1))
        sunMat.setAmbient(VBase4(1, 1, 0, 1))
        sunMat.setEmission(VBase4(0.5, 0.5, 0, 1))
        sunMat.setSpecular(VBase4(0.6, 0.2, 0, 1))
        #sunMat.setTwoside(True)
        
        
        # Starting with the sun.
        self.sun = loader.loadModel(dummySphere)
        self.sun.setMaterial(sunMat)
        self.sun.reparentTo(self.sunNode)
        self.sun.setPos(0,0,0)
        self.sun.setScale(sunData[1])
        
        
        # Mercury = Planet 1.
        self.mercury = loader.loadModel(dummySphere)
        self.mercury.reparentTo(self.planet1Node)
        self.mercury.setPos((planet1Data[0] + sunHalf) * orbitDis, 0 ,0)
        self.mercury.setScale(planet1Data[1])
        
        # Venus = Planet 2.
        self.venus = loader.loadModel(dummySphere)
        self.venus.reparentTo(self.planet2Node)
        self.venus.setPos((planet2Data[0] + sunHalf) * orbitDis, 0, 0)
        self.venus.setScale(planet2Data[1])
        
        # Earth = Planet 3.
        self.earth = loader.loadModel(dummySphere)
        self.earth.reparentTo(self.planet3Node)
        self.earth.setPos((planet3Data[0] + sunHalf) * orbitDis, 0, 0)
        self.earth.setScale(planet3Data[1])
        print self.earth.getPos()
        
        # Mars = Planet 4.
        self.mars = loader.loadModel(dummySphere)
        self.mars.reparentTo(self.planet4Node)
        self.mars.setPos((planet4Data[0] + sunHalf) * orbitDis, 0, 0)
        self.mars.setScale(planet4Data[1])
        
        # Jupiter = Planet 5.
        self.jupiter = loader.loadModel(dummySphere)
        self.jupiter.reparentTo(self.planet5Node)
        self.jupiter.setPos((planet5Data[0] + sunHalf) * orbitDis, 0, 0)
        self.jupiter.setScale(planet5Data[1])
        
        # Saturn = Planet 6.
        self.saturn = loader.loadModel(dummySphere)
        self.saturn.reparentTo(self.planet6Node)
        self.saturn.setPos((planet6Data[0] + sunHalf) * orbitDis, 0, 0)
        self.saturn.setScale(planet6Data[1])
        
        # Uranus = Planet 7.
        self.uranus = loader.loadModel(dummySphere)
        self.uranus.reparentTo(self.planet7Node)
        self.uranus.setPos((planet7Data[0] + sunHalf) * orbitDis, 0, 0)
        self.uranus.setScale(planet7Data[1])
        
        # Neptune = Planet 8.
        self.neptune = loader.loadModel(dummySphere)
        self.neptune.reparentTo(self.planet8Node)
        self.neptune.setPos((planet8Data[0] + sunHalf) * orbitDis, 0, 0)
        self.neptune.setScale(planet8Data[1])
        
        # Pluto = Planet 9.
        self.pluto = loader.loadModel(dummySphere)
        self.pluto.reparentTo(self.planet9Node)
        self.pluto.setPos((planet9Data[0] + sunHalf) * orbitDis, 0, 0)
        self.pluto.setScale(planet9Data[1])
        
        # planets END.
        
    # SYSTEM1 END.
    



#--------------------------------------------------------------------->
































