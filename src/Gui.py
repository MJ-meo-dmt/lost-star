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
from panda3d.core import Filename
from panda3d.core import PandaNode, NodePath, Camera, TextNode
from panda3d.core import Point3, Vec3, Vec4, BitMask32
from panda3d.core import ColorBlendAttrib
from panda3d.core import Filename, Buffer, Shader
# TASK
from direct.task import Task
# PANDAC
from pandac.PandaModules import *
# DIRECT
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
# EXTRA
import random, sys, os, math

##
# Game Imports
#
#from playerControl import playerControl

###########################
########## CODE ###########
##########################

class Gui(DirectObject):
    
    def genLabelText(self, text, i):
            return OnscreenText(text = text, pos = (-1.3, .95-.05*i), fg=(1,1,1,1),
                                align = TextNode.ALeft, scale = .05, mayChange = 1)
    
    
    def __init__(self):
        
    
        #Things to note:
        #-fg represents the forground color of the text in (r,g,b,a) format
        #-pos  represents the position of the text on the screen.
        #      The coordinate system is a x-y based wih 0,0 as the center of the
        #      screen
        #-align sets the alingment of the text relative to the pos argument.
        #      Default is center align.
        #-scale set the scale of the text
        #-mayChange argument lets us change the text later in the program.
        #       By default mayChange is set to 0. Trying to change text when
        #       mayChange is set to 0 will cause the program to crash.
        self.title = OnscreenText(text="Project: lost-star  v0.01 - 'Alpha'",
                              style=1, fg=(1,1,1,1),
                              pos=(-0.8,-0.95), scale = .07)
        self.testText = self.genLabelText("The Void", 0)
        


