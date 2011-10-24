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
        
        # Creating the Skybox
        self.skyBox=loader.loadModel("../resources/models/Skybox.egg") # The Skybox need a redo.
        self.skyBox.setScale(20,20,20) # Any size - No matter
        self.skyBox.setBin("background", 0);
        self.skyBox.setDepthWrite(False);
        self.skyBox.setCompass() # ?
        self.skyBox.setZ(render, 0)
                
        # Attach the Skybox to the Camera
        self.skyBox.reparentTo(base.camera)
        
        # Init Lights
        spaceLightsObj = SpaceLights()
        self.skyBox.setLightOff()
        
        # Load Space Station Data
        testSpaceStation = SpaceStationControl()
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


# EVERYTHING TO DO WITH SPACE STATIONS...
class SpaceStationControl:
        
        def __init__(self):
            
            # test model 
            self.Sstasion = loader.loadModel("../resources/models/SpaceStation.egg")
            #self.sstasion.setScale(0, 0, 0)
            self.Sstasion.setPos(0, 200, 0)
            self.Sstasion.reparentTo(render)
# END of SpaceStationControl CLASS.


