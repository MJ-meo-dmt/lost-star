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

#----->
# Sys Imports/Buildin.
import random, sys, os, math

# Config Load/import.
from config import *
from panda3d.core import loadPrcFile, loadPrcFileData

# Load devConfig file.

if (useDevmode == True):
    loadPrcFile(ConfData)
    print "+ Config Settings loaded..."
    print ""
    
# Config check Use Pstats.
if (usePstat == True):
    PStatClient.connect()
    print "+ Using Pstat Client..."
    
# Engine imports
print "+ Loading Engine..."
print "<---------------------------------------->"
import direct.directbase.DirectStart
print "<---------------------------------------->"
print ""

# CORE imports
from panda3d.core import WindowProperties
from panda3d.core import Filename
from panda3d.core import Camera
from panda3d.core import LightRampAttrib
from panda3d.core import ColorBlendAttrib
from panda3d.core import Filename,Buffer,Shader

# TASK imports
from direct.task import Task

# PANDAC imports
from pandac.PandaModules import *

# DIRECT imports
from direct.filter.CommonFilters import *
from direct.showbase.DirectObject import DirectObject

# Game Imports
from Galaxy import Galaxy
from Player import Player
from Gui import Gui


###########################
########### CODE #########
##########################

# World class. -MAIN-
class Main(DirectObject):

    def __init__(self):
		
		# Print Init.
        print ""
        print "#####################################"
        print "--  MAIN INIT --"
        print ""
        
        # Camera Settings.
        base.camLens.setFov(camFOV)
        base.camLens.setNear(camNear)
        base.camLens.setFar(camFar)
        print "Camera settings loaded..."
        
        # Shader & Filter settings.
        if useAutoShader == True:
            render.setShaderAuto()
            print "+ Using AutoShader..."
        
        # Set Filter.
        filters = CommonFilters(base.win, base.cam)
        
        # Set Bloom.
        if useBloom == True:
            setBloom = filters.setBloom(blend=(0.8,0.8,0.8,1), desat=-0.5, intensity=4.0, size="small")
            print "+ Using Bloom..."
            
        # Set CartoonInk.
        if useCartoonInk == True:
            filters.setCartoonInk()
            print "+ Using CartoonInk()"
            
        # Set Antialias.
        if useAntialias == True:
            render.setAntialias(AntialiasAttrib.MAuto)
            print "+ Using Antialias(Mauto)"
            
        #--------------------------------------->
        # RUN OUTER MAIN CLASSES.
        init_Galaxy = Galaxy()
        init_Gui = Gui()
        init_PlayerControl = Player()
        
        
        #-------------------------------------<
        
         # STATS SETTINGS
        
        # Use Analyzer.
        if useAnalyze == True:
            print ""
            print "##############################>"
            print "## ANALYZE DATA ##"
            print "###########################"
            print ""
            render.analyze()

### END OF MAIN CLASS

Main()
print "= RUNNING ="
run()
