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


###########################
########## CODE ###########
##########################

class Galaxy(DirectObject):
    
    def __init__(self):
        
        # Init skyBox. "aka spaceBox"
        self.skyBox=loader.loadModel("../resources/models/Skybox.egg") # The Skybox need a redo.
        self.skyBox.setScale(20,20,20) # Any size - No matter
        self.skyBox.setBin("background", 0)
        self.skyBox.setDepthTest(False)
        self.skyBox.setCompass() # ?
        self.skyBox.setZ(render, 0)
        
        # Attach the Skybox to the base.camera.
        self.skyBox.reparentTo(base.camera)
        
        # Init Lights
        spaceLightsInit = SpaceLights()
        self.skyBox.setLightOff()
        
        # Init Planet Creation
        PlanetInit = Planets()
        PlanetInit.planetSpawn()
        
        # Load Space Station Data
        #testSpaceStation = SpaceStationControl()
# END of Galaxy CLASS.


# SpaceLights
class SpaceLights:
    
    def __init__(self):
        
        # LIGHTS
        # lets add hdr lighting for fun
        render.setShaderAuto()
        #render.setAttrib(LightRampAttrib.makeHdr1())
        ambientLight = AmbientLight("ambientLight")
        # existing lighting is effectively darkened so boost ambient a bit
        ambientLight.setColor(Vec4(.4, .4, .4, 1))
        
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(Vec3(-5, -5, -5))
        # hdr can handle any amount of lighting
        # lets make things nice and sunny
        directionalLight.setColor(Vec4(2.0, 2.0, 2.0, 1.0))
        directionalLight.setSpecularColor(Vec4(2.0, 2.0, 2.0, 1))
        
        render.setLight(render.attachNewNode(ambientLight))
        render.setLight(render.attachNewNode(directionalLight))
# END of SpaceLights CLASS


# EVERYTHING TO DO WITH SPACE STATIONS. Here will be subclasses.
class SpaceStationControl:
    
    def __init__(self):
        
        # test model 
        self.Sstasion = loader.loadModel("../resources/models/SpaceStation.egg")
        #self.sstasion.setScale(0, 0, 0)
        self.Sstasion.setPos(0, 200, 0)
        self.Sstasion.reparentTo(render)
# END of SpaceStationControl CLASS.


# Planet control and creation.
class Planets(Galaxy):
    
    def __init__(self):
        
        # Space scale " var " 
        self.galaxyScale = 100.0 # Global scale for size
        self.orbitscale = 10000 # AU - To exact scale

    def planetSpawn(self):
        
        # Here is the code for the creation of the planets
        
        self.orbit_root_mercury = render.attachNewNode('orbit_root_mercury')
        self.orbit_root_venus = render.attachNewNode('orbit_root_venus')
        self.orbit_root_mars = render.attachNewNode('orbit_root_mars')
        self.orbit_root_earth = render.attachNewNode('orbit_root_earth')

        self.orbit_root_moon = (self.orbit_root_earth.attachNewNode('orbit_root_moon'))

        # Generic Planet load
        self.genericPlanet = "../resources/models/planet_sphere.egg"
        
        
        self.sun = loader.loadModel(self.genericPlanet)
        self.sun_tex = loader.loadTexture("../resources/models/textures/planets/lowRes/sun_1k_tex.jpg")
        self.sun.setTexture(self.sun_tex, 1)
        self.sun.reparentTo(render)
        self.sun.setScale(4 * self.galaxyScale)

        self.mercury = loader.loadModel(self.genericPlanet)
        self.mercury_tex = loader.loadTexture("../resources/models/textures/planets/lowRes/mercury_1k_tex.jpg")
        self.mercury.setTexture(self.mercury_tex, 1)
        self.mercury.reparentTo(self.orbit_root_mercury)
        self.mercury.setPos( 0.38 * self.orbitscale, 0, 0)
        self.mercury.setScale(0.385 * self.galaxyScale)

        self.venus = loader.loadModel(self.genericPlanet)
        self.venus_tex = loader.loadTexture("../resources/models/textures/planets/lowRes/venus_1k_tex.jpg")
        self.venus.setTexture(self.venus_tex, 1)
        self.venus.reparentTo(self.orbit_root_venus)
        self.venus.setPos( 0.72 * self.orbitscale, 0, 0)
        self.venus.setScale(0.923 * self.galaxyScale)

        self.mars = loader.loadModel(self.genericPlanet)
        self.mars_tex = loader.loadTexture("../resources/models/textures/planets/lowRes/mars_1k_tex.jpg")
        self.mars.setTexture(self.mars_tex, 1)
        self.mars.reparentTo(self.orbit_root_mars)
        self.mars.setPos( 1.52 * self.orbitscale, 0, 0)
        self.mars.setScale(0.515 * self.galaxyScale)

        self.earth = loader.loadModel(self.genericPlanet)
        self.earth_tex = loader.loadTexture("../resources/models/textures/planets/lowRes/earth_1k_tex.jpg")
        self.earth.setTexture(self.earth_tex, 1)
        self.earth.reparentTo(self.orbit_root_earth)
        self.earth.setScale(self.galaxyScale)
        self.earth.setPos( self.orbitscale, 0, 0)

        self.orbit_root_moon.setPos( self.orbitscale, 0, 0)

        self.moon = loader.loadModel(self.genericPlanet)
        self.moon_tex = loader.loadTexture("../resources/models/textures/planets/lowRes/moon_1k_tex.jpg")
        self.moon.setTexture(self.moon_tex, 1)
        self.moon.reparentTo(self.orbit_root_moon)
        self.moon.setScale(0.1 * self.galaxyScale)
        self.moon.setPos(0.1 * self.orbitscale, 0, 0)





























