import os
add_library('minim')
player = Minim(this)

path = os.getcwd()
#`This constant just manages which portal is about to be launched from portal gun it can either be 0 or 1
PORTALNB = 0
#used to progress levels
LVLNB = 0
DOORENTRD = True




#creature class from which the player inherits
class Creature:
    def __init__(self, x, y, r, g):
        # x coordinate of creature
        self.x = x
        # y coordinate of creature
        self.y = y
        # "radius" of the creature
        self. r = r
        #ground of creature
        self. g = g
        #y velocity of creature
        self.vy = 0
        #x velocity of creature
        self.vx = 0
        #temporary x and y velocities that are used in calculations later on
        self.tmpvy = 0
        self.tmpvx = 0
        
        
    #gravity method that is similiar to the one created for the mario game
    def gravity(self):
               
        
        #temporary ground variable will be used in the following code to be processed before assigning the actual ground to it.
        tmpg = game.g
        #for loop just makes sure that if the character is stepping on a floor surface, the surface is set as the temporary ground.
        for s in game.slist:
            if self.y + self.r <= s.y and self.x + self.r >= s.x and self.x - self.r <= s.x + s.l and  s.y < tmpg and s.place == "f":
                tmpg = s.y
       
        #this for loop deals with portal entry.(if a character enters a portal)
        for p in game.portals:
            
            #if statement just lists conditions of portal entry    
            if ((p.x - 20 <= self.x <= p.x + 20 and self.y == p.y - self.r and self.y < p.y and p.type == "h") or (sideentry(p))) and 0 < p.opt.x and 0 < p.opt.y:
                #portal entered attribute of the game is set to true
                game.pentered = True
                
                #sets the ground to the lowest part of the screen so character falls from portal.
                tmpg = game.h
                
                #the temporary velocities just store the velocities of the character right when the character enters the portal
                self.tmpvx = game.chell.vx
                self.tmpvy = game.chell.vy
                
                
                #sets the x and y coordinates of character to the x and y coordinates of the other portal(opt)
                self.y = p.opt.y
                self.x = p.opt.x
                
                #This chain of if conditions just checks in what orientation the other portal is (if it's on a left wall, right wall, etc.) to be able to transform the velocities of the character appropriately
                if p.opt.place == "lw":
                    self.tmpvx = ((self.tmpvx)**2+(self.tmpvy)**2)**0.5 + 7
                    
                elif p.opt.place == "rw":
                    self.tmpvx = -1*((self.tmpvx)**2+(self.tmpvy)**2)**0.5 - 7
                    
                elif p.opt.place == "c":
                    self.tmpvy = ((self.tmpvx)**2+(self.tmpvy)**2)**0.5
                
                elif p.opt.place == "f":
                    self.tmpvy = -1*((self.tmpvx)**2+(self.tmpvy)**2)**0.5 + 0.4
                
       
        #Sets the condition that if the character is on the ground and it has not entered a portal to stop vertical motion.
        if self.y + self.r >= self.g and game.pentered == False:
            self.vy = 0
        #if the portal has been entered then set the vertical velocity to the temporary velocity that was played around with in the previous lines of code.
        elif game.pentered:
            self.vy = self.tmpvy
        #else condition is for when character is not on the ground is falling, this code is like the mario game code
        else:
            
            self.vy += 0.4
            
            if self.y + self.r + self.vy > self.g:
                self.vy = self.g - (self.y+self.r)
         
         #updates the character's ground with the temporary ground variable   
        self.g = tmpg
        
        
    #update function which has a similiar purpose like in the mario game.
    def update(self):
        
        #this part just updates the x and y positions using the velocities
        self.gravity()
        self.y += self.vy
        self.x += self.vx
        
            
    #standard display fucntion that was used for testing which used to display a circle
    def display(self):    
        self.update()
        # circle(self.x, self.y, self.r * 2)

#this chell class is the creature that the player controls (it's called chell in reference to the main character of the portal games)
#We had a creature and chell class in the hopes that we would have time to make turrets or enemeies but we didn't have the time.
class Chell(Creature):
    #inheritence from the creature class
    def __init__(self, x, y, r, g):
        Creature.__init__(self, x, y, r, g)
        #these extra attributes are unique to the chell class becuase it is being controlled
        self.controls = {LEFT:False, RIGHT:False, UP:False}
        #the spritesheet is imported here
        self.img = loadImage(path + "/walksheet.png")
        #the waking slice attribute is used for the walking animation
        self.wslice = 0
        #the idle slice attribute is used for the idle animation
        self.islice = 0
        #the frames attribute serves the same purpose as the one in the mario game.
        self.frames = 3
        #image width and height attributes
        self.img_w = 40
        self.img_h = 40
        #instantiates the direction of the character to face to the right
        self.direction = RIGHT
  
    #this display function has all the naimation for the chell class  
    def display(self):   
        self.update()
        
        #nested if conditions to determine which animation to play
        
        #this if is for when its idle and facing the left
        if self.vx == 0 and self.vy == 0 and self.direction == LEFT:
            image(self.img,self.x - self.img_w//2,self.y - self.img_h//2,self.img_w,self.img_h,(self.islice + 1)*self.img_w,0,self.islice*self.img_w,self.img_h)
        
        #this one is for one it's idle and to the right
        elif self.vx == 0 and self.vy == 0 and self.direction == RIGHT:
            image(self.img,self.x - self.img_w//2,self.y - self.img_h//2,self.img_w,self.img_h,self.islice*self.img_w,0,(self.islice + 1)*self.img_w,self.img_h)
        
        #this one is for when it's moving to the right
        elif self.direction == RIGHT:
            image(self.img,self.x - self.img_w//2,self.y - self.img_h//2,self.img_w,self.img_h,self.wslice*self.img_w,0,(self.wslice + 1)*self.img_w,self.img_h)
        
        #this one is for when it's moving to the left
        elif self.direction == LEFT:
            image(self.img,self.x - self.img_w//2,self.y - self.img_h//2,self.img_w,self.img_h,(self.wslice + 1)*self.img_w,0,self.wslice*self.img_w,self.img_h)
        
    def update(self):
        self.gravity()
        
        # If the portal was entered it maintains the momentum by setting the horizontal velocity to the one calculated in the gravity method
        if game.pentered == True:
            self.vx = self.tmpvx
            self.tmpvx = 0
            #afterwards it resets the portal entered attribute to false
            game.pentered = False
        
        #deals with input to cause motion in the case a portal was not entered
        
        elif self.controls[LEFT] == True:
            self.vx = -5
            self.direction = LEFT
        elif self.controls[RIGHT] == True:
            self.vx = 5
            self.direction = RIGHT
        #if no keys where pressed and the character is on the ground (which is characterized by the vertical velocity being 0) and it did not just enter a portal the character stops moving horizontally
        elif self.vy == 0:
            self.vx = 0
            
        
        #Just deals with the "jumping"
        if self.controls[UP] == True and self.y+self.r == self.g:
            self.vy = -7
        
        
        #updates positions
        self.y += self.vy
        self.x += self.vx
        
        #These if conditons just cause the slice to change to get the feeling of animations in the game.
        
        #this if is for when the character is walking
        if frameCount % 5 == 0 and self.vx != 0 and self.vy == 0:
            self.wslice = (self.wslice + 1)% self.frames + 3
        #this elif is for when the character is idle
        elif frameCount % 10 == 0 and self.vx == 0 and self.vy == 0:
            self.islice = (self.islice + 1)% self.frames
        
        #This just deals with collision with vertical walls and prevents the character from phasing through walls
        for s in game.slist:
            #Handles door entry
            if s.isDoor and s.type == "v" and s.place == "rw" and distance(self.x, self.y, s.x, self.y) <= self.r and self.x + self.r >= s.x and self.y + self.r <= s.y +s.l and self.y - self.r >= s.y:
                global LVLNB
                global DOORENTRD
                DOORENTRD = True
                LVLNB = (LVLNB + 1) % 3
            
            if s.type == "v" and s.place == "rw" and distance(self.x, self.y, s.x, self.y) <= self.r and self.x + self.r >= s.x and self.y + self.r <= s.y +s.l and self.y - self.r >= s.y:
                self.x = s.x - self.r
                
            if s.type == "v" and s.place == "lw" and distance(self.x, self.y, s.x, self.y) <= self.r and self.x - self.r <= s.x and self.y + self.r <= s.y +s.l and self.y - self.r >= s.y:
                self.x = s.x + self.r
 
 
       
             
#This surface class is the backbone of the portal mechanics in the game. It is the game's guide on where to have collisions, place portals, and which orientation the portals are in.
class Surface:
    def __init__(self, x, y, l, place,type = "h", blocked = False, isDoor = False):
        #x coordinate of the surface
        self.x = x
        #y coordinate of the surface
        self.y = y
        #length of the surface
        self.l = l
        #type of surface (horizontal or vertical)
        self.type = type
        #place of the surface (left wall, right wall, floor, or ceiling)
        self.place = place
        #blocked just states if the surface is blocked from having portals on it or not.
        self.blocked = blocked
        
        self.isDoor = isDoor
    
    # the display fucntion is used purely for level design and devolpment. it represents surface by a line.
    def display(self):
        return
        # stroke(0)
        # if self.type == "h":
        #     strokeWeight(1)
        #     line(self.x,self.y,self.x+self.l,self.y)
        # else:
        #     strokeWeight(1)
        #     line(self.x,self.y,self.x,self.y+self.l)



        
#the portals class is self explanatory just the class representing the portals.
class Portal:
    def __init__(self,x,y,type,nb):
        #coordinates of portals
        self.x = x
        self.y = y
        #type of portal (horizontal or vertical)
        self.type = type
        #the other portal attribute just stores the other portal object (there are only 2 portals at a time)
        self.opt = None
        #the portal's number (0 or 1)
        self.nb = nb
        #the place on which the portal is on (ceiling, floor, etc.), its instantiated by none but later when portals are being fired it will be assigned appropriately
        self.place = None
    

    
    #display method for the portals
    def display(self):
        
        #If conditions to represent the portals based on their type (horizontal/vertical) and their number (portal 0 is blue and portal 1 is orange)
        if self.nb == 0 and self.type == "h":
            stroke(0,191,255)
            strokeWeight(5)
            line(self.x-20, self.y, self.x+20, self.y)
        elif self.nb == 0 and self.type == "v":
            stroke(0,191,255)
            strokeWeight(5)
            line(self.x,self.y-20,self.x,self.y+20)
        elif self.nb == 1 and self.type == "h":
            stroke(255,165,0)
            strokeWeight(5)
            line(self.x-20, self.y, self.x+20, self.y)
        elif self.nb == 1 and self.type == "v":
            stroke(255,165,0)
            strokeWeight(5)
            line(self.x,self.y-20,self.x,self.y+20)
        

#The game class which acts as a container for the games' various objects
class Game:
    def __init__(self, w, h, g, lvlnb):
        #background music attribute
        self.bgm1 = player.loadFile(path+"/bgm1.mp3")
        self.bgm1.play()
        #level number attribute
        self.lvlnb = lvlnb
        #the games' portal list
        self.portals = []
        #instantiation of the portals outside the screen
        self.portals.append(Portal(-1*w, -1*h,"h",0))
        self.portals.append(Portal(-1*w, -1*h,"h",1))
        #assigning the other portals to each portal
        self.portals[0].opt = self.portals[1]
        self.portals[1].opt = self.portals[0]
        #background image depending on level
        if self.lvlnb == 0:
            self.bg = loadImage(path + "/lvl1.png")
        elif self.lvlnb == 1:
            self.bg = loadImage(path + "/lvl2.png")
        #width and height of the game
        self.w = w
        self.h = h
        #the game's default ground
        self.g = g
        #the portal entry attribute
        self.pentered = False
        
        #instantion of the player
        if self.lvlnb == 0:
            self.chell = Chell(100,500,20,self.g)
        elif self.lvlnb == 1:
            self.chell = Chell(50,300,20,self.g)
        # the game's surface list
        self.slist = []
        if self.lvlnb == 0:
            self.slist.append(Surface(58,66,586,"lw","v"))
            self.slist.append(Surface(58,652,420,"f","h"))
            self.slist.append(Surface(808,652,420,"f","h"))
            self.slist.append(Surface(58,66,486,"c","h"))
            self.slist.append(Surface(735,66,486,"c","h"))
            self.slist.append(Surface(1221,66,460,"rw","v"))
            self.slist.append(Surface(478,312,340,"rw","v"))
            self.slist.append(Surface(478,310,330,"f","h"))
            self.slist.append(Surface(808,312,340,"lw","v"))
            
            #door
            self.slist.append(Surface(1230,530,135,"rw","v", True, True))
        elif self.lvlnb == 1:
            self.slist.append(Surface(0,380,145,"f","h"))
            self.slist.append(Surface(0,220,135,"c","h"))
            self.slist.append(Surface(158,0,200,"lw","v"))
            self.slist.append(Surface(0,200,180,"lw","v", True))
            self.slist.append(Surface(145,380,309,"lw","v"))
            self.slist.append(Surface(145,689,185,"f","h"))
            self.slist.append(Surface(330,689,170,"f","h", True))
            self.slist.append(Surface(500,375,309,"rw","v", True))
            self.slist.append(Surface(510,380,780,"f","h", True))
            #door
            self.slist.append(Surface(1280,74,306,"rw","v", True, True))
            
        
        # portal coordinates dictionary used later to temporarily store the coordinates of the portals
        self.portalcoord = {"x":-1*self.w,"y":-1*self.h}
    
    
    #arguably the most complex method, it is used to determine where a portal is placed in the event the mouse is clicked.
    def portal_pos(self):
        #temporary coodinates that will be modified in the following code
        tmpcoord = {"x":-1*self.w,"y":-1*self.h}
        #For loop uses a mathematical formula I developed to get the coordinates of the point that is in line with the character and the mouse and lies on the nearest surface
        for s in self.slist:
            if s.type == "v" and mouseX != self.chell.x and mouseY != self.chell.y:
                Y = ((((self.h-mouseY)-(self.h-self.chell.y))/(mouseX - self.chell.x))*(s.x - self.chell.x)) + (self.h - self.chell.y)
                Y = self.h - Y
                if in_surface(s.x,Y,s) and (distance(self.chell.x,self.chell.y,tmpcoord["x"],tmpcoord["y"]) > distance(self.chell.x,self.chell.y, s.x, Y)) and samesign(mouseX-self.chell.x, s.x - self.chell.x) and samesign(mouseY - self.chell.y, Y - self.chell.y):
                    tmpcoord["x"] = s.x
                    tmpcoord["y"] = Y
            elif s.type == "h" and mouseX == self.chell.x:
                tmpcoord["x"] = mouseX
                tmpcoord["y"] = s.y
                
            elif s.type == "v" and mouseY == self.chell.y:
                tmpcoord["x"] = s.x
                tmpcoord["y"] = mouseY
            
            elif s.type == "h" and mouseX != self.chell.x and mouseY != self.chell.y :
                X = (((self.h-s.y)-(self.h-self.chell.y))/((self.h-mouseY)-(self.h-self.chell.y)))*(mouseX-self.chell.x) + self.chell.x
                if in_surface(X,s.y,s) and distance(self.chell.x,self.chell.y,tmpcoord["x"],tmpcoord["y"]) > distance(self.chell.x,self.chell.y, X, s.y) and samesign(mouseX-self.chell.x, X - self.chell.x) and samesign(mouseY - self.chell.y, s.y - self.chell.y):
                    tmpcoord["x"] = X
                    tmpcoord["y"] = s.y
        
        #sets the portal coordinates to the one's calculated in the for loop
        self.portalcoord["x"] = tmpcoord["x"]
        self.portalcoord["y"] = tmpcoord["y"]
    

    
    #display method of the game just displays all objects in order
    def display(self):
        
        self.chell.display()
        
        for s in self.slist:
            s.display()
        
        for p in self.portals:
            p.display()
#instantiation of the game class

game = Game(1280, 720, 700, LVLNB)

def setup():
    size(game.w, game.h)
    background(255, 255, 255)

def draw():
    global DOORENTRD
    global game
    #For the playable levels
    if LVLNB < 2:
        if DOORENTRD == True:
            game = Game(1280, 720, 720, LVLNB)
            DOORENTRD = False
        
        
        
        #hides the cursor to show a portal shaped cursor instead that shows which color the portal you are about to shoot is gonna have.
        noCursor()
        
        background(255, 255, 255)
        image(game.bg,0,0,1280,720)
        
        #game display
        game.display()
        
        # portal shaped cursor
        if PORTALNB == 0:
            stroke(0,191,255)
            strokeWeight(2)
            noFill()
            ellipse(mouseX,mouseY, 10, 15)
        else:
            stroke(255,165,0)
            strokeWeight(2)
            noFill()
            ellipse(mouseX,mouseY, 10, 15)
            
        #tutorial text for the first level
        if game.lvlnb == 0:
            textSize(25)
            text("Use Arrow Keys to move", 490, 350)
            text("Use mouse to aim portals", 490, 400)
            text("Click to shoot", 490, 450)
            text("Press R to reset portals", 490, 500)
            text("Jump into one portal and", 490, 550)
            text("come out of the other!", 490, 580)
            text("Get to the door!", 490, 630)
    #Win screen code
    else:
        background(0)
        cursor()
        textSize(60)
        
        text("Thank you for playing our game! :)", 150, 300)
        textSize(20)
        text("Click to restart", 500, 430)
    
#handles keyboard input
def keyPressed():
    if keyCode == LEFT:
        game.chell.controls[LEFT] = True
    elif keyCode == RIGHT:
        game.chell.controls[RIGHT] = True
    elif keyCode == UP:
        game.chell.controls[UP] = True
        
    if key == "R" or key == "r":
        game.portals[0].x = -1*game.w
        game.portals[0].y = -1*game.h
        game.portals[1].x = -1*game.w
        game.portals[1].y = -1*game.h
    
def keyReleased():
    if keyCode == LEFT:
        game.chell.controls[LEFT] = False
        game.chell.vx = 0
    elif keyCode == RIGHT:
        game.chell.controls[RIGHT] = False
        game.chell.vx = 0
    elif keyCode == UP:
        game.chell.controls[UP] = False   

        
#handles the portal "firing" in case the mouse is pressed        
def mouseClicked():
    global PORTALNB
    global LVLNB
    if LVLNB < 2:
        game.portal_pos()
        
        #conditions to place a portal
        if (outofboundary(game.portalcoord["x"],game.portalcoord["y"]) is False) and (game.portalcoord["x"] > game.portals[1-PORTALNB].x + 30 or game.portalcoord["x"] < game.portals[1-PORTALNB].x - 30 or game.portalcoord["y"] < game.portals[1-PORTALNB].y - 30 or game.portalcoord["y"] > game.portals[1-PORTALNB].y + 30) : 
            for s in game.slist:
    
                if in_surface(game.portalcoord["x"],game.portalcoord["y"], s) and not s.blocked:
                    game.portals[PORTALNB].type = s.type
                    game.portals[PORTALNB].place = s.place
                    game.portals[PORTALNB].x = game.portalcoord["x"]
                    game.portals[PORTALNB].y = game.portalcoord["y"]
                    PORTALNB = (PORTALNB + 1)%2
                    
                    
    else:
        LVLNB = 0
                
#fucntion that checks if a point lies on a surface used in the portal_pos method
def in_surface(n,m,s):

    if s.x <= n and n <= (s.x + s.l) and s.y == m and s.type == "h":
        return True
    elif ((s.y <= m) and (m <= (s.y + s.l)) and (s.x == n) and (s.type == "v")):
        return True
    
    return False
      
    
#function used to calculate distance between 2 points used in the portal_pos method
def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

#function that checks if 2 numbers have the same sign used to make sure portal is on the same side as the mouse
def samesign(n1,n2):
    if n1>0 and n2>0:
        return True
    elif n1<0 and n2<0:
        return True
    return False

#checks if a portal has been entered sideways
def sideentry(port):
    
    for p in game.portals:
        
        if ((game.chell.x - game.chell.r == p.x and p.place == "lw" and game.chell.vx < 0 and p.y - 20 <= game.chell.y <= p.y + 20) or (game.chell.x + game.chell.r == p.x and p.place == "rw" and game.chell.vx > 0 and p.y - 20 <= game.chell.y <= p.y + 20)) and p == port:
            return True
        
    return False

#checks if a portal is going to lie beyond the limits of surface used in the mouseclicked function
def outofboundary(x,y):
    
    for s in game.slist:
        if ((x + 20 > s.x + s.l and s.type == "h" and y == s.y and in_surface(x,y,s)) or (x - 20 < s.x and s.type == "h" and y == s.y and in_surface(x,y,s)) or (y + 20 > s.y + s.l and s.type == "v" and x == s.x and in_surface(x,y,s)) or (y - 20 < s.y and s.type == "v" and x == s.x and in_surface(x,y,s))):
            return True
    
    return False
 
