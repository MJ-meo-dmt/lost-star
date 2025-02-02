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

# System Imports
import sys, os, random, math

# Panda Imports


####>  MAIN CONFIG   <####
print "Loading Main Config..."

### PATHS ###

# Config.prc path.
CONFIG_PRC = "../config/Config.prc"

# Database config.
DB_PATH = "db/gameData.db"

# Skybox path.
SKYBOX_PATH = "../resources/models/GenericSkybox.egg"
####>


##  DEVELOPMENT EXTRAS  ##
useConfigPrc = True
usePstats = True

## CAMERA SETTINGS  ##
camFov = 70
camNear = 0.05
camFar = 1000000
###>


## VIDEO SETTINGS  ##
useAutoShader = True
useBloom = False
useCartoonInk = False
useAntialias = False
useAnalyze = True
###>


##  DATABASE IDs  ##

# Table IDs.
col0 = 'planetName'
col1 = 'planetDis'
col2 = 'planetScale'
col3 = 'planetPosX'
col4 = 'planetPosY'
col5 = 'planetPosZ'
###>

## SCALE VARIABLES ##
# Set the variables for scale and distance changes; (like global var)
ORBIT_DIS = 30 # This is the 30cm from the model. (From the scale pdf, ask me)
SUN_HALF = 1.5 # This is sunScale / 2 and cheated to fit in with rest of the scale/slash/Distance (needs work!)
print "Main Config Loaded >>>"
















