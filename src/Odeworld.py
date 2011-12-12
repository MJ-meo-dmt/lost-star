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
import direct.directbase.DirectStart
from pandac.PandaModules import OdeWorld, OdeBody, OdeMass, Quat
from direct.task import Task
from direct.showbase.DirectObject import DirectObject

# Config (game).
from config import *

# Database Import.
from db import *

####>  CODE   <####

groundPlain = loader.loadModel("../resources/models/plane.egg")
groundPlain.reparentTo(render)
groundPlain.setPos(0, 0, 0)

box = loader.loadModel("../resources/models/box.egg")
box.reparentTo(render)
box.setPos(0, 0, 10)

physics = OdeWorld()
physics.setGravity(0, 0, -9.81)  # This is the default setting for earths gravity.  This will certainly change.


myBody = OdeBody(physics)
myMass = OdeMass()
myMass.setBox(11340, 1, 1, 1) # This will change just for testing.


myBody.setMass(myMass)
myBody.setPosition(box.getPos(render))
myBody.setQuaternion(box.getQuat(render))


deltaTimeAccumulator = 0.0
stepSize = 1.0 / 90.0


def simulationTask(task):
    global deltaTimeAccumulator
    
    myBody.setForce(1, min(task.time**2 * 800000 - 800000, 0), 0)
    deltaTimeAccumulator += globalClock.getDt()
    while deltaTimeAccumulator > stepSize:
        deltaTimeAccumulator -= stepSize
        physics.quickStep(stepSize)
    
    box.setPosQuat(render, myBody.getPosition(), Quat(myBody.getQuaternion()))
    return task.cont

taskMgr.doMethodLater(1.0, simulationTask, "Physics Simulation")





run()




































