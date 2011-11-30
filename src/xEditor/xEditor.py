#!/usr/bin/python

##########################################
###									######
###		THE VOID					######
###		PROJECT : lost-star			######
###		0x7dc 'EDEN'				######
###									######
##########################################

# DEVELOPERS

# 	* MJ-me0-dmt  -  
# 
# NOTES !!
# I adjusted the gui text acording to my screen size on the laptop.
# 
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

# Sys, os Imports
import sys, os, math


# Config File
from pandac.PandaModules import *
loadPrcFileData("setup", """
sync-video 1
show-frame-rate-meter #t
win-size 800 600
#win-size 1024 768
#win-size 1280 800
#win-size 1280 1024
#win-fixed-size 1
#yield-timeslice 0 
#client-sleep 0 
#multi-sleep 0
#basic-shaders-only #t
fullscreen #f
#audio-library-name null
want-directtools #f
want-tk #f
""")

# Engine Imports.
import direct.directbase.DirectStart
from direct.filter.CommonFilters import CommonFilters
from panda3d.core import Filename,Buffer,Shader
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *
from pandac.PandaModules import Material
from pandac.PandaModules import VBase4

# Set Background color black.
base.setBackgroundColor(0,0,0,0)

# Setup basic filters.
filters = CommonFilters(base.win, base.cam)

################################
#######       SCRIPTING PART      ##########
#######      COPY FROM HERE    ###########
#################################

# Setting up custom materials.
mat1 = Material()
mat1.setShininess(2.0)
mat1.setDiffuse(VBase4(1,1,0,1))
mat1.setAmbient(VBase4(1,1,0,1))
mat1.setEmission(VBase4(1,1,0,1))
mat1.setSpecular(VBase4(0.8,0.6,0,1))
mat1.setTwoside(True)



solarSystem1 = render.attachNewNode('solarSystem1')
sun1 = solarSystem1.attachNewNode('sun1')
planet1 = sun1.attachNewNode('planet1')
planet2 = sun1.attachNewNode('planet2')
planet3 = sun1.attachNewNode('planet3')
planet4 = sun1.attachNewNode('planet4')
planet5 = sun1.attachNewNode('planet5')
planet6 = sun1.attachNewNode('planet6')
planet7 = sun1.attachNewNode('planet7')
planet8 = sun1.attachNewNode('planet8')
planet9 = sun1.attachNewNode('planet9')

dummySphere = "models/planet_sphere"


# ----------------------------------------->>
# Global Variables for Scale.

spaceDis = 30 # From the pdf 30cm.
sunDispi = 0.9424 # Sun pi something weird...


sun = loader.loadModel(dummySphere)
sun.setMaterial(mat1)
sun.reparentTo(sun1)
sun.setScale(30.00)
sun.setPos(0,0,0)

mercury = loader.loadModel(dummySphere)
mercury.reparentTo(planet1)
mercury.setPos((0.76 + sunDispi)* spaceDis,0,0)
mercury.setScale(0.10)

venus = loader.loadModel(dummySphere)
venus.reparentTo(planet2)
venus.setPos((1.42+ sunDispi)* spaceDis,0,0)
venus.setScale(0.26)

earth = loader.loadModel(dummySphere)
earth.reparentTo(planet3)
earth.setPos((1.97+ sunDispi)* spaceDis,0,0)
earth.setScale(0.27)

mars = loader.loadModel(dummySphere)
mars.reparentTo(planet4)
mars.setPos((3.00+ sunDispi)* spaceDis,0,0)
mars.setScale(0.15)# 1.5cm

jupiter = loader.loadModel(dummySphere)
jupiter.reparentTo(planet5)
jupiter.setPos((10.25+ sunDispi)* spaceDis,0,0)
jupiter.setScale(3.00)# 

saturn = loader.loadModel(dummySphere)
saturn.reparentTo(planet6)
saturn.setPos((18.80+ sunDispi)* spaceDis,0,0)
saturn.setScale(2.50)

uranus = loader.loadModel(dummySphere)
uranus.reparentTo(planet7)
uranus.setPos((37.80+ sunDispi)* spaceDis,0,0)
uranus.setScale(1.00)

neptune = loader.loadModel(dummySphere)
neptune.reparentTo(planet8)
neptune.setPos((59.20+ sunDispi)* spaceDis,0,0)
neptune.setScale(0.98)

pluto = loader.loadModel(dummySphere)
pluto.reparentTo(planet9)
pluto.setPos((77.80+ sunDispi)* spaceDis,0,0)
pluto.setScale(0.05)#0.005

###
##  EXTRA MODELS
### 

# Plane background.

#plane = loader.loadModel("./models/xyzViewPlane.egg")
#plane.reparentTo(render)
#plane.setPos(0,0,-52)

#######################################
#########           SCRIPTING END           ############
#########            COPY TO HERE           ############
########################################
    
    
    
def printText(name, message, color): 
    text = TextNode(name) # create a TextNode. Note that 'name' is not the text, rather it is a name that identifies the object.
    text.setText(message) # Here we set the text of the TextNode
    x,y,z = color # break apart the color tuple
    text.setTextColor(x,y,z, 1) # Set the text color from the color tuple
    text3d = NodePath(text) # Here we create a NodePath from the TextNode, so that we can manipulate it 'in world'
    text3d.reparentTo(render) # So that its centred on the object
    
    text3d.setScale(1.5, 1.5, 1.5) # Adjust the size of the axis xyz
    
    return text3d # return the NodePath for further use
   
#Also note that we are going up in increments of 1 and then sub 1 for all 3 axis.
# +
for i in range(0,51):
    printText("X", "|", (1,0,0)).setPos(i,0,0)  # note that "X" is the name of the TextNode, not its content. 
# -
for i in range(0,51):
    printText("X", "|", (1,0,0)).setPos(-i,0,0)
# +
for i in range(0,51):
    printText("Y", "|", (0,1,0)).setPos(0,i,0)  
# -
for i in range(0,51):
    printText("Y", "|", (0,1,0)).setPos(0,-i,0)
# +
for i in range(0,51):
    printText("Z", "-", (0,0,1)).setPos(0,0,i) 
# -
for i in range(0,51):
    printText("Z", "-", (0,0,1)).setPos(0,0,-i)

# Add the X Y Z to the ends of the axis.
# First (0,0,0) is color.
printText("XL", "X", (0,0,0)).setPos(51,0,-1.5)
printText("YL", "Y", (0,0,0)).setPos(-1.5,51,0) 
printText("YL", "Z", (0,0,0)).setPos(-1.5,0,51) 
printText("OL", "0", (0,0,0)).setPos(-1.2,0,-1.2) 

# Backwards
printText("XL", "X", (0,0,0)).setPos(-51,0,-1.5)
printText("YL", "Y", (0,0,0)).setPos(-1.5,-51,0) 
printText("YL", "Z", (0,0,0)).setPos(-1.5,0,-51)



# OnscreenText function, which is derived from TextNode.
# It is restricted to 2D

# Gather Data for INFO: Outputs
#mScale = str(m.getScale()) # Get main object scale
#mPos = str(m.getPos()) # Get main object Position
#mGeo = SceneGraphAnalyzer()# Geo data output * need Fix!!
print "----------------------------"
#print "SceneGraph output : \n",mGeo
print "----------------------------"

# TITLE
OnscreenText(text="xEditor", style=2,  fg=(1,1,1,1), pos=(1.0,-0.9), scale = .07)
OnscreenText(text="Solar-system Viewer", style=2,  fg=(1,1,1,1), pos=(-1.6,0.9), scale = .06)

# INFO
#OnscreenText(text="- Object Scale : %s" % mScale, style=2,  fg=(1,1,1,1), pos=(-1.35,0.84), scale = .052)
#OnscreenText(text="- Object Pos : %s" % mPos, style=2,  fg=(1,1,1,1), pos=(-1.35,0.78), scale = .052)
# NOTES
OnscreenText(text="Notes:", style=2,  fg=(1,1,1,1), pos=(-1.6,-0.6), scale = .05)
OnscreenText(text="1pu = 0.1m = 10cm", style=2,  fg=(1,1,1,1), pos=(-1.4,-0.65), scale = .05)



# Create Light
#----------------------------------------------------------------------------------->

# Setup Ambient light
ambientLight = AmbientLight("ambientLight")
ambientLight.setColor(Vec4(0.1, 0.1, 0.1, 1))
render.setLight(render.attachNewNode(ambientLight))

# Adding Sun light.
plight = PointLight('plight')
plight.setColor(VBase4(1, 1, 0.8, 1))
#plight.setAttenuation(Point3(0.9,0, 0))
sunLight = render.attachNewNode(plight)
sunLight.setPos(0,0,0)
sunLight.setScale(3.0)
sun1.setLight(sunLight)


#----------------------------------------------------------------------------------->

# Extra Settings.

# Set shaders to auto. 
render.setShaderAuto()

# Setup HDR lighting.
# hdr can handle any amount of lighting
render.setAttrib(LightRampAttrib.makeHdr1())

# Set Bloom
filterBloom = filters.setBloom(blend=(0.8,0.8,0.8,1), desat=-0.5, intensity=4.0, size="small")

# Camera Extra.
#base.camera.setPos(5,-30,5)
#base.camera.lookAt(m)


# Loop
run()
