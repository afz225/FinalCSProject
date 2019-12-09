import os

path = os.getcwd()
PORTALNB = 0

class Creature:
    def __init__(self, x, y, r, g):
        self.x = x
        self.y = y
        self. r = r
        self. g = g
        self.vy = 0
        self.vx = 0
        self.tmpvy = 0
        self.tmpvx = 0
        self.wallentered = False
        
    def gravity(self):
               
        
        
        tmpg = game.g
        for s in game.slist:
            if self.y + self.r <= s.y and self.x + self.r >= s.x and self.x - self.r <= s.x + s.l and  s.y < tmpg and s.type == "h":
                tmpg = s.y
       
        for p in game.portals:
                
            if (p.x - 20 <= game.chell.x <= p.x + 20 and game.chell.y == p.y - game.chell.r and game.chell.y < p.y and p.type == "h") or (sideentry(p)):
                game.pentered = True
                


                tmpg = game.h
                
                # if game.chell.y >= p.y:
                
                self.tmpvx = game.chell.vx
                self.tmpvy = game.chell.vy
                

                game.chell.y = p.opt.y
                game.chell.x = p.opt.x
                
                
                
                print(game.pentered)
                if p.opt.place == "lw":
                    self.tmpvx = ((self.tmpvx)**2+(self.tmpvy)**2)**0.5 + 5
                    print(self.tmpvx)
                    
                elif p.opt.place == "rw":
                    self.tmpvx = -1*((self.tmpvx)**2+(self.tmpvy)**2)**0.5 - 5
                    
                elif p.opt.place == "c":
                    self.tmpvy = ((self.tmpvx)**2+(self.tmpvy)**2)**0.5
                elif p.opt.place == "f":
                    self.tmpvy = -1*((self.tmpvx)**2+(self.tmpvy)**2)**0.5 + 0.4
                
                self.wallentered = False
       
        
        if self.y + self.r >= self.g and game.pentered == False:
            self.vy = 0
        elif game.pentered:
            self.vy = self.tmpvy
    
        else:
            self.vy += 0.4
            
            if self.y + self.r + self.vy > self.g:
                self.vy = self.g - (self.y+self.r)
                
        self.g = tmpg
        
        
        
    def update(self):
        
        
        self.gravity()
        self.y += self.vy
        self.x += self.vx
        
        for s in game.slist:
            if (s.place == "f" and game.chell.y <= p.y and game.chell.y + game.chell.r >= p.y) or (s.place == "f" and game.chell.y >= p.y and (game.chell.y - game.chell.r) <= p.y):
                game.chell.y = p.y - game.chell.r
        
            
    
    def display(self):    
        self.update()
        # circle(self.x, self.y, self.r * 2)

class Chell(Creature):
    def __init__(self, x, y, r, g):
        Creature.__init__(self, x, y, r, g)
        self.controls = {LEFT:False, RIGHT:False, UP:False}
        self.img = loadImage(path + "/walksheet.png")
        self.wslice = 0
        self.islice = 0
        self.frames = 3
        self.img_w = 40
        self.img_h = 40
        self.direction = RIGHT
        
    def display(self):   
        self.update()
        # circle(self.x, self.y, self.r * 2)
        
        if self.vx == 0 and self.vy == 0 and self.direction == LEFT:
            image(self.img,self.x - self.img_w//2,self.y - self.img_h//2,self.img_w,self.img_h,(self.islice + 1)*self.img_w,0,self.islice*self.img_w,self.img_h)
        elif self.vx == 0 and self.vy == 0 and self.direction == RIGHT:
            image(self.img,self.x - self.img_w//2,self.y - self.img_h//2,self.img_w,self.img_h,self.islice*self.img_w,0,(self.islice + 1)*self.img_w,self.img_h)
        elif self.direction == RIGHT:
            image(self.img,self.x - self.img_w//2,self.y - self.img_h//2,self.img_w,self.img_h,self.wslice*self.img_w,0,(self.wslice + 1)*self.img_w,self.img_h)
        elif self.direction == LEFT:
            image(self.img,self.x - self.img_w//2,self.y - self.img_h//2,self.img_w,self.img_h,(self.wslice + 1)*self.img_w,0,self.wslice*self.img_w,self.img_h)
        
    def update(self):
        self.gravity()
        
        if game.pentered == True:
            self.vx = self.tmpvx
            self.tmpvx = 0
            game.pentered = False
        
        elif self.controls[LEFT] == True:
            self.vx = -5
            self.direction = LEFT
        elif self.controls[RIGHT] == True:
            self.vx = 5
            self.direction = RIGHT
        elif self.vy == 0:
            self.vx = 0
        # else:
            
        
        
        if self.controls[UP] == True and self.y+self.r == self.g:
            self.vy = -12
        
        
        
        self.y += self.vy
        self.x += self.vx
        
        if frameCount % 5 == 0 and self.vx != 0 and self.vy == 0:
            self.wslice = (self.wslice + 1)% self.frames + 3
        elif frameCount % 10 == 0 and self.vx == 0 and self.vy == 0:
            self.islice = (self.islice + 1)% self.frames
        
        for s in game.slist:
            if s.type == "v" and s.place == "rw" and distance(self.x, self.y, s.x, self.y) <= self.r and self.x + self.r >= s.x and self.y + self.r <= s.y +s.l and self.y - self.r >= s.y:
                self.wallentered = True
                self.x = s.x - self.r
                
            if s.type == "v" and s.place == "lw" and distance(self.x, self.y, s.x, self.y) <= self.r and self.x - self.r <= s.x and self.y + self.r <= s.y +s.l and self.y - self.r >= s.y:
                self.x = s.x + self.r
                self.wallentered = True
    
    
class Surface:
    def __init__(self, x, y, l, place,type = "h"):
        self.x = x
        self.y = y
        self.l = l
        self.type = type
        self.place = place
        
    def display(self):
        s = ""
        # stroke(0)
        # if self.type == "h":
        #     strokeWeight(1)
        #     line(self.x,self.y,self.x+self.l,self.y)
        # else:
        #     strokeWeight(1)
        #     line(self.x,self.y,self.x,self.y+self.l)

class Portal:
    def __init__(self,x,y,type,nb):
        self.x = x
        self.y = y
        self.type = type
        self.opt = None
        self.nb = nb
        self.place = None
    

    
    def display(self):
        
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
        

class Game:
    def __init__(self, w, h, g):
        self.portals = []
        
        self.portals.append(Portal(-1*w, -1*h,"h",0))
        self.portals.append(Portal(-1*w, -1*h,"h",1))
        self.portals[0].opt = self.portals[1]
        self.portals[1].opt = self.portals[0]
        self.bg = loadImage(path + "/lvl1.png")
        self.w = w
        self.h = h
        self.g = g
        self.pentered = False
        self.chell = Chell(100,500,20,self.g)
        self.slist = []
        self.slist.append(Surface(58,66,586,"lw","v"))
        self.slist.append(Surface(58,652,420,"f","h"))
        self.slist.append(Surface(808,652,420,"f","h"))
        self.slist.append(Surface(58,66,486,"c","h"))
        self.slist.append(Surface(735,66,486,"c","h"))
        self.slist.append(Surface(1221,66,460,"rw","v"))
        self.slist.append(Surface(478,312,340,"rw","v"))
        self.slist.append(Surface(478,310,330,"f","h"))
        self.slist.append(Surface(808,312,340,"lw","v"))
        
        # self.slist.append(Surface(100,100,1280,"c","h"))
        # self.slist.append(Surface(100,700,1280,"f","h"))
        # self.slist.append(Surface(300, 600, 300,"f", "h"))
        # self.slist.append(Surface(700, 500, 300,"f","h"))
        # self.slist.append(Surface(1000, 0, 700,"rw","v"))
        
                
        self.portalcoord = {"x":-1*self.w,"y":-1*self.h}
    
    
    def portal_pos(self):
        tmpcoord = {"x":-1*self.w,"y":-1*self.h}
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
        
        self.portalcoord["x"] = tmpcoord["x"]
        self.portalcoord["y"] = tmpcoord["y"]
    

    
    
    def display(self):
        
        self.chell.display()
        
        for s in self.slist:
            s.display()
        
        for p in self.portals:
            p.display()
game = Game(1280, 720, 700)
def setup():
    size(game.w, game.h)
    background(255, 255, 255)
def draw():
    background(255, 255, 255)
    image(game.bg,0,0,1280,720)
    
    game.display()

def keyPressed():
    if keyCode == LEFT:
        game.chell.controls[LEFT] = True
    elif keyCode == RIGHT:
        game.chell.controls[RIGHT] = True
    elif keyCode == UP:
        game.chell.controls[UP] = True
    
def keyReleased():
    if keyCode == LEFT:
        game.chell.controls[LEFT] = False
        game.chell.vx = 0
    elif keyCode == RIGHT:
        game.chell.controls[RIGHT] = False
        game.chell.vx = 0
    elif keyCode == UP:
        game.chell.controls[UP] = False   
        
def mouseClicked():
    global PORTALNB
    game.portal_pos()
    
    print(outofboundary(game.portalcoord["x"],game.portalcoord["y"]))
    
    if (outofboundary(game.portalcoord["x"],game.portalcoord["y"]) is False) and (game.portalcoord["x"] > game.portals[1-PORTALNB].x + 30 or game.portalcoord["x"] < game.portals[1-PORTALNB].x - 30 or game.portalcoord["y"] < game.portals[1-PORTALNB].y - 30 or game.portalcoord["y"] > game.portals[1-PORTALNB].y + 30) : 
        for s in game.slist:
            if in_surface(game.portalcoord["x"],game.portalcoord["y"], s):
                game.portals[PORTALNB].type = s.type
                game.portals[PORTALNB].place = s.place
        game.portals[PORTALNB].x = game.portalcoord["x"]
        game.portals[PORTALNB].y = game.portalcoord["y"]
        PORTALNB = (PORTALNB + 1)%2
        
    print(PORTALNB)
      
def in_surface(n,m,s):

    if s.x <= n and n <= (s.x + s.l) and s.y == m and s.type == "h":
        return True
    elif ((s.y <= m) and (m <= (s.y + s.l)) and (s.x == n) and (s.type == "v")):
        return True
    
    return False
      
    

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def samesign(n1,n2):
    if n1>0 and n2>0:
        return True
    elif n1<0 and n2<0:
        return True
    return False

def sideentry(port):
    
    for p in game.portals:
        
        if ((game.chell.x - game.chell.r == p.x and p.place == "lw" and game.chell.vx < 0 and p.y - 20 <= game.chell.y <= p.y + 20) or (game.chell.x + game.chell.r == p.x and p.place == "rw" and game.chell.vx > 0 and p.y - 20 <= game.chell.y <= p.y + 20)) and p == port:
            return True
        
    return False

def outofboundary(x,y):
    
    for s in game.slist:
        if (x + 20 > s.x + s.l and s.type == "h" and y == s.y and in_surface(x,y,s)) or (x - 20 < s.x and s.type == "h" and y == s.y and in_surface(x,y,s)) or (y + 20 > s.y + s.l and s.type == "v" and x == s.x and in_surface(x,y,s)) or (y - 20 < s.y and s.type == "v" and x == s.x and in_surface(x,y,s)):
            return True
        
    
    return False
