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
from panda3d.core import WindowProperties, Camera
from panda3d.core import loadPrcFile, loadPrcFileData
from direct.filter.CommonFilters import *
from direct.showbase.DirectObject import DirectObject

# Config (game).
from config import *

# Database Import.
from db import *

# Game Imports.
import Galaxy
import Player

####>  CODE   <####

## ENGINE PRC CONFIG EXTRAS ##

# LOAD PRC.
if (useConfigPrc == True):
    loadPrcFile(CONFIG_PRC)
    print "+ CONFIG LOADED +"
    print ""
    
# USE Pstats.
if (usePstats == True):
    PStatClient.connect()
    print "+ PSTAT ENABLED +"



### MAIN CLASS ###
# This will call and run everything.

class Main(ShowBase, DirectObject):
    
    def __init__(self):
        ShowBase.__init__(self)
        
        ## Print to Console.
        print "Starting Main..."
        
        ## SETUP CONFIGS ##
        
        # Camera Settings.
        base.camLens.setFov(camFov)
        base.camLens.setNear(camNear)
        base.camLens.setFar(camFar)
        print "- Camera settings loaded..."
        
        # Shader & Filter settings.
        if useAutoShader == True:
            render.setShaderAuto()
            print "- AutoShader ENABLED..."
            
        # Bloom Settings.
        if useBloom == True:
            filters = CommonFilters(base.win, base.cam)
            BloomFilter = filters.setBloom(blend=(0.8, 0.8, 0.8, 1), desat=-0.4, intensity=3.0, size="small")
            
        ### INIT GAME CLASSES ###
        
        Galaxy.Galaxy()
        Player.Player()
        
        # Analyzer.
        if useAnalyze == True:
            print "----------------------------------------------------"
            render.analyze()
            
            print ">--------------------------------------------------"
            print "PRINTING RENDER NODES"
            print "--------------->>>"
            print render.ls()
            
        
# INIT Main game.
startGame = Main()

# LOOP
startGame.run()
