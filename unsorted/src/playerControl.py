# Use in GALAXY CLASS

# ORIGIN OF CODE
'''
### Original Header
#iModels: Jeff Styers, Reagan Heller

# Last Updated: 6/13/2005
#
# This tutorial provides an example of creating a character
# and having it walk around on uneven terrain, as well
# as implementing a fully rotatable camera.

### Better Ralph: modifications by Stephen Lujan
# This is a modification of the roaming ralph demo to provide improved controls
# and camera angles, imitating those of modern commercial games
'''


SPEED = 1.0
# PlayerControl class, KB + Mouse + Camera and player SHIP
class playerControl(DirectObject):
    
    def genLabelText(self, text, i):
            return OnscreenText(text = text, pos = (-1.3, .95-.05*i), fg=(1,1,1,1),
                                align = TextNode.ALeft, scale = .05, mayChange = 1)
                                
    def __init__(self):
        
        self.controlMap = {"left":0, "right":0, "forward":0, "backward":0,
            "zoom-in":0, "zoom-out":0, "wheel-in":0, "wheel-out":0}
        self.mousebtn = [0,0,0]
        base.win.setClearColor(Vec4(0,0,0,1))
        
        # Accept the control keys for movement and rotation

        self.accept("escape", sys.exit)
        self.accept("w", self.setControl, ["forward",1])
        self.accept("a", self.setControl, ["left",1])
        self.accept("s", self.setControl, ["backward",1])
        self.accept("d", self.setControl, ["right",1])
        self.accept("w-up", self.setControl, ["forward",0])
        self.accept("a-up", self.setControl, ["left",0])
        self.accept("s-up", self.setControl, ["backward",0])
        self.accept("d-up", self.setControl, ["right",0])
#        self.accept("mouse1", self.setControl, ["zoom-in", 1])
#        self.accept("mouse1-up", self.setControl, ["zoom-in", 0])
#        self.accept("mouse3", self.setControl, ["zoom-out", 1])
#        self.accept("mouse3-up", self.setControl, ["zoom-out", 0])
        self.accept("wheel_up", self.setControl, ["wheel-in", 1])
        self.accept("wheel_down", self.setControl, ["wheel-out", 1])
        self.accept("page_up", self.setControl, ["zoom-in", 1])
        self.accept("page_up-up", self.setControl, ["zoom-in", 0])
        self.accept("page_down", self.setControl, ["zoom-out", 1])
        self.accept("page_down-up", self.setControl, ["zoom-out", 0])

        taskMgr.add(self.move,"moveTask")

        
        # Game state variables
        self.isMoving = False

        # Set up the camera
        # Adding the camera to Player ship
        
        base.camera.reparentTo(self.playerShip)
        # POV of camera
        # This value serve as a vertical offset.
        self.cameraTargetHeight = 6.0
        # How far should the camera be from Ship
        self.cameraDistance = 30
        # Initialize the pitch of the camera
        self.cameraPitch = 10
        # Disable basic mouse control.
        base.disableMouse()
        # The mouse moves rotates the camera so lets get rid of the cursor
        props = WindowProperties()
        props.setCursorHidden(True)
        base.win.requestProperties(props)
       

        # Create some lighting
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
        


    #Records the state of the arrow keys
    def setControl(self, key, value):
        self.controlMap[key] = value


    # Accepts arrow keys to move either the player or the menu cursor,
    # Also deals with grid checking and collision detection
    def move(self, task):

        # save ralph's initial position so that we can restore it,
        # in case he falls off the map or runs into something.

        startpos = self.playerShip.getPos()
        
        # Player ship speed
        shipSpeed = 120
        
        # If a move-key is pressed, move ship in the specified direction.
        if (self.controlMap["forward"]!=0):
            self.playerShip.setY(self.playerShip, -shipSpeed * globalClock.getDt())
        if (self.controlMap["backward"]!=0):
            self.playerShip.setY(self.playerShip, shipSpeed * globalClock.getDt())
        if (self.controlMap["left"]!=0):
            self.playerShip.setX(self.playerShip, shipSpeed * globalClock.getDt())
        if (self.controlMap["right"]!=0):
            self.playerShip.setX(self.playerShip, -shipSpeed * globalClock.getDt())

        # If a zoom button is pressed, zoom in or out
        if (self.controlMap["wheel-in"]!=0):
            self.cameraDistance -= 0.1 * self.cameraDistance;
            if (self.cameraDistance < 5):
                self.cameraDistance = 5
            self.controlMap["wheel-in"] = 0
        elif (self.controlMap["wheel-out"]!=0):
            self.cameraDistance += 0.1 * self.cameraDistance;
            if (self.cameraDistance > 250):
                self.cameraDistance = 250
            self.controlMap["wheel-out"] = 0
        if (self.controlMap["zoom-in"]!=0):
            self.cameraDistance -= globalClock.getDt() * self.cameraDistance;
            if (self.cameraDistance < 5):
                self.cameraDistance = 5
        elif (self.controlMap["zoom-out"]!=0):
            self.cameraDistance += globalClock.getDt() * self.cameraDistance;
            if (self.cameraDistance > 250):
                self.cameraDistance = 250

            
            
        # Use mouse input to turn both ship and the Camera
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
            self.playerShip.setH(self.playerShip.getH() - mouseSpeed* deltaX)
            self.playerShip.setH(self.playerShip.getH() - mouseSpeed* deltaX)
            
            self.playerShip.setP(self.playerShip.getP() + mouseSpeed* deltaY)
            self.playerShip.setP(self.playerShip.getP() + mouseSpeed* deltaY)
            
            
            
            # find the new camera pitch and clamp it to a reasonable range
            self.cameraPitch = self.cameraPitch + 0.1 * deltaY
            if (self.cameraPitch < -60): self.cameraPitch = -60
            if (self.cameraPitch >  80): self.cameraPitch =  80
            base.camera.setHpr(0,self.cameraPitch,0)
            
            # set the camera at around middle of the ship
            # We should pivot around here instead of the view target which is noticebly higher
            base.camera.setPos(0,0,self.cameraTargetHeight/2)
            # back the camera out to its proper distance
            base.camera.setY(base.camera,self.cameraDistance)

        # point the camera at the view target
        viewTarget = Point3(0,0,self.cameraTargetHeight)
        base.camera.lookAt(viewTarget)
        
        return task.cont 
    # Get and print out playerShip POS - GPS
    
