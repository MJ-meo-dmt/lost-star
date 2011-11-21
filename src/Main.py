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

# Load Config File

from panda3d.core import loadPrcFile
 
loadPrcFile("../config/Config.prc")


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
from Galaxy import Galaxy
from Player import Player
from Gui import Gui


###########################
########## CODE ###########
##########################

# World class. -MAIN-
class Main(DirectObject):

    def __init__(self):
		
		# Random check test.
        print "Test Hello"
        
        # Just for now..
        base.camLens.setNear(0.05)
        base.camLens.setFar(1000000)
        base.camLens.setFov(90)
        
        render.setShaderAuto()
        # Filters working on supported VGA GPU's only
        filters = CommonFilters(base.win, base.cam)
        #filters.setBloom()
        filters.setCartoonInk()
        #
        
        #render.setAntialias(AntialiasAttrib.MAuto)
### END OF MAIN CLASS

# CLASS CALLS (INIT)
GameMain = Main()
init_Galaxy = Galaxy()
init_Gui = Gui()
init_PlayerControl = Player()


run()
