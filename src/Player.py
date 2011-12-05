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
from panda3d.core import WindowProperties
from direct.task import Task
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject

# Config (game).
from config import *

# Database Import.
from db import *

####>  CODE   <####

# Player Class handle player/s related things.
class Player(DirectObject):
    
    def __init__(self):
        
        # INIT PLAYER CLASSES.
        PlayerControl()
    

# PLAYER Class END.


class PlayerShip:
    def __init__(self):
        # Load Ship Model
        self.playerLoad()
        
    def playerLoad(self):
		# Load the player model.
		# Will add db functionality later...  
        # Create a node for the playerShip.
        self.playerShipNode = render.attachNewNode('PlayerShip')
        # self.playerSpawnNode = render.attachNewNode('Player Spawn')
        
        # Load the model itself.
        self.playerShip = Actor("../resources/models/scout_Ship.egg")  # Should create a db_table for ships, items e.g
        self.playerShip.reparentTo(self.playerShipNode)
        self.playerShip.setPos(103.9, 0.5, 0)
        self.playerShip.setScale(0.05)  # Should be 0.001 | The smallest planet(pluto) has the size of 0.05.

# PLAYERSHIP Class END.   


class PlayerControl(DirectObject):
    def __init__(self):
        
        # INIT Needed things.
        # Inst. for Player Class playership.
        initPlayerShip = PlayerShip()
        self.playershipOB = initPlayerShip.playerShip
        
        
        ### SETUP CONTROL MAPS  ###
        self.controlMap = {"left": 0, "right": 0, "forward": 0, "backward": 0, "wheel-in": 0, "wheel-out": 0}
                           
        self.mousebtn = [0, 0, 0]
        
        
        ### SETUP KEYBOARD ###
        # Setup the control [KEYS] for movement w,a,s,d. | This is basic will have to adjust for advance controls.
        self.accept("escape", sys.exit)
        self.accept("w", self.setControl, ["forward", 1])
        self.accept("a", self.setControl, ["left", 1])
        self.accept("s", self.setControl, ["backward", 1])
        self.accept("d", self.setControl, ["right", 1])
        
        self.accept("w-up", self.setControl, ["forward", 0])
        self.accept("a-up", self.setControl, ["left", 0])
        self.accept("s-up", self.setControl, ["backward", 0])
        self.accept("d-up", self.setControl, ["right", 0])
        
        # Setup mouse [ZOOM].
        self.accept("wheel_up", self.setControl, ["wheel-in", 1])
        self.accept("wheel_down", self.setControl, ["wheel-out", 1])
        
        # Add the "moveTask"
        taskMgr.add(self.move, "moveTask")
        
        # Game State Variable.
        self.IsMoving = False
        ###>
        
        ###  SETUP CAMERA  ###
        # Reparent the -main- Camera to PlayerShip.
        base.camera.reparentTo(self.playershipOB)
        
        # The vertical offset.  To view over ship.
        self.cameraHeight = 0.05
        
        # Camera Distance from playerShip. On Start.
        self.cameraDistance = 0.23
        
        # Camera Pitch.
        self.cameraPitch = 0.04
        
        # Disable the basic camera controls.
        base.disableMouse()
        
        # This should be used together with a right click function, for the camera rotate. Like in wow.
        WinProps = WindowProperties()
        # Hide the cursor. | This will change with the rightClick function. 
        # Giving us the cursor when not rotating. If the player wants to rotate basic [KEYS] left/right can turn while cursor is active.
        WinProps.setCursorHidden(True) 
        base.win.requestProperties(WinProps)
        ###>
        
    # Check the state of the KB.
    def setControl(self, key, value):
        self.controlMap[key] = value
        
    ###>
    
    def move(self, task):
        
        # Movement Speed for playerShip.
        movementSpeed = 1
        
        # Check if a-move key is pressed, if so move.
        # Forward.
        if (self.controlMap["forward"] != 0):
            self.playershipOB.setY(self.playershipOB, -movementSpeed * globalClock.getDt())
        # Backward.
        if (self.controlMap["backward"] != 0):
            self.playershipOB.setY(self.playershipOB, movementSpeed * globalClock.getDt())
        # Left.
        if (self.controlMap["left"] != 0):
            self.playershipOB.setX(self.playershipOB, movementSpeed * globalClock.getDt())
        # Right.
        if (self.controlMap["right"] != 0):
            self.playershipOB.setX(self.playershipOB, -movementSpeed * globalClock.getDt())
        
        # Check for zooming and Do.
        if (self.controlMap["wheel-in"] != 0):
            self.cameraDistance -= 0.1 * self.cameraDistance
            if  (self.cameraDistance < 0.01):
                self.cameraDistance = 0.01
            self.controlMap["wheel-in"] = 0
        
        elif (self.controlMap["wheel-out"] != 0):
            self.cameraDistance += 0.1 * self.cameraDistance
            if (self.cameraDistance > 250):
                self.cameraDistance = 250
            self.controlMap["wheel-out"] = 0
            
            
        # Make use of mouse, to turn playerShip and the Camera.
        if base.mouseWatcherNode.hasMouse():
            
            # get changes in mouse position
            md = base.win.getPointer(0)
            x = md.getX()
            y = md.getY()
            
            deltaX = md.getX() - 200
            deltaY = md.getY() - 200
            
            # reset mouse cursor position
            base.win.movePointer(0, 200, 200)
            
            # Mouse speed setting
            mouseSpeed = 0.15
            
            # alter the ship's yaw by an amount proportionate to deltaX
            self.playershipOB.setH(self.playershipOB.getH() - mouseSpeed* deltaX)
            self.playershipOB.setH(self.playershipOB.getH() - mouseSpeed* deltaX)
            
            self.playershipOB.setP(self.playershipOB.getP() + mouseSpeed* deltaY)
            self.playershipOB.setP(self.playershipOB.getP() + mouseSpeed* deltaY)
            
            
            
            # find the new camera pitch and clamp it to a reasonable range
            self.cameraPitch = self.cameraPitch + 0.1 * deltaY
            if (self.cameraPitch < -60): self.cameraPitch = -60
            if (self.cameraPitch >  80): self.cameraPitch =  80
            base.camera.setHpr(0,self.cameraPitch,0)
            
            # set the camera at around middle of the ship
            # We should pivot around here instead of the view target which is noticebly higher
            base.camera.setPos(0,0,self.cameraHeight/2)
            # back the camera out to its proper distance
            base.camera.setY(base.camera,self.cameraDistance)

        # point the camera at the view target
        viewTarget = Point3(0,0,self.cameraHeight)
        base.camera.lookAt(viewTarget)
        
        
        return task.cont   
        
    
    ###>
# PLAYERCONTROL Class END


# Npc Class handle AI.
class Npc:
    
    def __init__(self):
        pass 

#  NPC Class END.


class Faction:
    
    def __init__(self):
        pass 

# FACTION Class END.

