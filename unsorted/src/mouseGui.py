##########################################
###									######
###		THE VOID					######
###		PROJECT : lost-star			######
###		0x7dc 'EDEN'				######
###									######
##########################################

# DEVELOPERS

# 	* MJ-me0-dmt  -  
# 	* ???

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

from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import * 
from direct.task import Task
from direct.interval.IntervalGlobal import *
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage

import sys

class mouseGui:
	def __init__(self):
		
		self.crosshair = loader.loadModel('../models/gui/cursor.egg')
		self.crosshairTexture = loader.loadTexture("../models/gui/textures/crosshair.png")
		self.crosshair.setTexture(self.crosshairTexture,1)
		self.crosshair.setTransparency(TransparencyAttrib.MAlpha)

		self.dummyNP = render2d.attachNewNode('crosshair')
		self.crosshair.reparentTo(self.dummyNP)
		self.crosshair.setScale(0.03,0,0.04)
		self.crosshair.setPos(0,5,0)
		self.crosshair.setColor(0.8,0.85,1,1)
		base.mouseWatcherNode.setGeometry(self.dummyNP.node())
		
		self.crosshair2 = loader.loadModel('../models/gui/cursor.egg')
		self.crosshair2.reparentTo(render2d)
		self.crosshair2Texture = loader.loadTexture("../models/gui/textures/aimSmall.png")
		self.crosshair2.setTexture(self.crosshair2Texture,1)
		self.crosshair2.setTransparency(TransparencyAttrib.MAlpha)
		#self.interval = LerpHprInterval(self.crosshair2, 2, (0,0,360))
		#self.interval.loop()
		
		
		self.dummyNP2 = render2d.attachNewNode('crosshair2')
		self.crosshair2.reparentTo(self.dummyNP2)
		self.crosshair2.setScale(0.03,0,0.04)
		self.crosshair2.setPos(0.03,5,-0.035)
		self.crosshair2.setColor(0.8,0.85,1,1)
		
		self.crosshair.setBin("gui-popup", 100)
		self.crosshair2.setBin("gui-popup", 100)
		
		
		self.mode = 1 # or 1
		self.toggle()
		
	def setMode(self, n=0):
		if n != self.mode:
			self.mode = n
			if n == 0:
				base.mouseWatcherNode.setGeometry(self.dummyNP.node())
				#self.crosshair2.detachNode()
				self.crosshair2.hide()
				self.crosshair.show()
				#self.crosshair.reparentTo(self.dummyNP)
			else:
				base.mouseWatcherNode.setGeometry(self.dummyNP2.node())
				#self.crosshair.detachNode()
				self.crosshair2.show()
				self.crosshair.hide()
				#self.crosshair2.reparentTo(self.dummyNP2)
				
		
	def toggle(self):
		if self.mode == 0:
			self.setMode(1)
		else:
			self.setMode(0)
		
			
if __name__ == "__main__":
	m = mouseGui()
	DO = DirectObject()
	DO.accept("mouse3", m.toggle)
	DO.accept("escape", sys.exit)
	run()
