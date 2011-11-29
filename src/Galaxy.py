##########################################
###									######
###		THE VOID					######
###		PROJECT : lost-star			######
###		0x7dc 'EDEN'				######
###									######
##########################################
# Start: early Oct. 2011

# DEVELOPERS

# 	* MJ-me0-dmt  - 1


#-->

# License
'''
Free BSD license 3-clause

Copyright (c)<2011>, <Martin de Bruyn>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    - Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    - Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    - Neither the name of the <organization> nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

#-->

# Engine imports
import direct.directbase.DirectStart
# CORE
from panda3d.core import WindowProperties
from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import CollisionTube,CollisionSegment
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Point3,Vec3,Vec4,BitMask32
from panda3d.core import LightRampAttrib
from panda3d.core import ColorBlendAttrib
from panda3d.core import Filename,Buffer,Shader

# TASK
from direct.task import Task
# PANDAC
from pandac.PandaModules import *
# DIRECT
from direct.filter.CommonFilters import *
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
# EXTRA
import random, sys, os, math

##
# Game Imports
#
from db import *
from config import *


###########################
########## CODE ###########
##########################

class Galaxy(DirectObject):
    
    def __init__(self):
        # Print Init.
        print ""
        print "#####################################"
        print "--  GALAXY LOADED --"
        print ""
        
        # DB Testing
        
        
        # Init skyBox. "aka spaceBox"
        self.skyBox=loader.loadModel("../resources/models/Skybox.egg") # The Skybox need a redo.
        self.skyBox.setScale(1.0,1.0,1.0) # Any size - No matter
        self.skyBox.setBin("background", 0)
        self.skyBox.setDepthTest(False)
        self.skyBox.setCompass() # ?
        self.skyBox.setZ(render, 0)
        print "+ Space Loaded..."
        
        # Attach the Skybox to the base.camera.
        self.skyBox.reparentTo(base.camera)
        
        # Init Lights
        spaceLightsInit = SpaceLights()
        #spaceLightsInit.lightSetup()
        self.skyBox.setLightOff()
        
        # Init Planet Creation
        self.PlanetInit = Planets()
        self.PlanetInit.earthPlanet()
        
        #Load Space Station Data
        #testSpaceStation = SpaceStationControl()

# END OF Galaxy CLASS.


# SpaceLights
# Everything todo with lights in space.#
class SpaceLights():
    
    def __init__(self):
        pass
        # Create Light
        #----------------------------------------------------------------------------------->
    def lightSetup():
        
        planetInit = Planets()
        sun1 = planetInit.earthPlanet.sun1()
        
        # Setup Ambient light
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(0.1, 0.1, 0.1, 1))
        render.setLight(render.attachNewNode(ambientLight))

        # Adding Sun light.
        plight = PointLight('plight')
        plight.setColor(VBase4(0.5, 0.5, 0.5, 1))
        #plight.setAttenuation(Point3(0.9,0, 0))
        sunLight = sun1.attachNewNode(plight)
        self.sunLight.setPos(0,0,0)
        render.setLight(sunLight)
    

#----------------------------------------------------------------------------------->

# END OF SpaceLights CLASS

# Planet control and creation.
class Planets(SpaceLights):
    
    def __init__(self):
        
        # Space scale " var " 
        self.galaxyScale = 4 # Global var for scaling, mainly Planets, Stars...
        self.galaxyDistance = 0.100
        
        
    def earthPlanet(self):
        
        # Here is the code for the creation of the planets
        DB = dbMain()
        
        #####
        ## PLANET LOAD.
        ##
        ##  THIS IS ONLY FOR TESTING NO SQL DATA IS EVEN BEING USED.
        ###
        
        # Setting up custom materials.
        self.mat1 = Material()
        self.mat1.setShininess(2.0)
        self.mat1.setDiffuse(VBase4(1,1,0,1))
        self.mat1.setAmbient(VBase4(1,1,0,1))
        self.mat1.setEmission(VBase4(1,1,0,1))
        self.mat1.setSpecular(VBase4(0.8,0.6,0,1))
        self.mat1.setTwoside(True)



        self.solarSystem1 = render.attachNewNode('solarSystem1')
        self.sun1 = self.solarSystem1.attachNewNode('sun1')
        self.planet1 = self.sun1.attachNewNode('planet1')
        self.planet2 = self.sun1.attachNewNode('planet2')
        self.planet3 = self.sun1.attachNewNode('planet3')
        self.planet4 = self.sun1.attachNewNode('planet4')
        self.planet5 = self.sun1.attachNewNode('planet5')
        self.planet6 = self.sun1.attachNewNode('planet6')
        self.planet7 = self.sun1.attachNewNode('planet7')
        self.planet8 = self.sun1.attachNewNode('planet8')
        self.planet9 = self.sun1.attachNewNode('planet9')
        
        
        dummySphere = "../resources/models/planet_sphere"

        self.sun = loader.loadModel(dummySphere)
        self.sun.setMaterial(self.mat1)
        self.sun.reparentTo(self.sun1)
        self.sun.setScale(3.0)
        self.sun.setPos(0,0,0)
        
        self.mercury = loader.loadModel(dummySphere)
        self.mercury.reparentTo(self.planet1)
        self.mercury.setPos((0.076*30)+ 4.712,0,0)
        self.mercury.setScale(0.01)

        self.venus = loader.loadModel(dummySphere)
        self.venus.reparentTo(self.planet2)
        self.venus.setPos((0.142*30)+ 4.712,0,0)
        self.venus.setScale(0.026)

        self.earth = loader.loadModel(dummySphere)
        self.earth.reparentTo(self.planet3)
        self.earth.setPos((0.197*30)+4.712,0,0)
        self.earth.setScale(0.027)

        self.mars = loader.loadModel(dummySphere)
        self.mars.reparentTo(self.planet4)
        self.mars.setPos((0.300*30)+4.712,0,0)
        self.mars.setScale(0.015)# 1.5cm

        self.jupiter = loader.loadModel(dummySphere)
        self.jupiter.reparentTo(self.planet5)
        self.jupiter.setPos((1.025*30)+4.712,0,0)
        self.jupiter.setScale(0.300)# 

        self.saturn = loader.loadModel(dummySphere)
        self.saturn.reparentTo(self.planet6)
        self.saturn.setPos((1.880*30)+4.712,0,0)
        self.saturn.setScale(0.250)

        self.uranus = loader.loadModel(dummySphere)
        self.uranus.reparentTo(self.planet7)
        self.uranus.setPos((3.780*30)+4.712,0,0)
        self.uranus.setScale(0.100)

        self.neptune = loader.loadModel(dummySphere)
        self.neptune.reparentTo(self.planet8)
        self.neptune.setPos((5.920*30)+4.712,0,0)
        self.neptune.setScale(0.098)

        self.pluto = loader.loadModel(dummySphere)
        self.pluto.reparentTo(self.planet9)
        self.pluto.setPos((7.780*30)+4.712,0,0)
        self.pluto.setScale(0.005)
       
    
### END OF Planets CLASS

# EVERYTHING TO DO WITH SPACE STATIONS. Here will be subclasses.
class Station:
    
    def __init__(self):
        
        
        # test model 
        self.Sstasion = loader.loadModel("../resources/models/SpaceStation.egg")
        #self.sstasion.setScale(0,0,0)
        self.Sstasion.setPos(0.14000,0.14000,0.0010) 
        self.Sstasion.reparentTo(render)
# END OF SpaceStationControl CLASS.



























