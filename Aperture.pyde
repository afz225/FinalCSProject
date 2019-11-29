
PORTALNB = 0

class Creature:
    def __init__(self, x, y, r, g):
        self.x = x
        self.y = y
        self. r = r
        self. g = g
        self.vy = 0
        self.vx = 0
        
    def gravity(self):
        
        
                
        if self.y + self.r >= self.g:
            self.vy = 0
        else:
            self.vy += 0.4
            
            if self.y + self.r + self.vy > self.g:
                self.vy = self.g - (self.y+self.r)
        
        tmpg = game.g
        for s in game.slist:
            if self.y + self.r <= s.y and self.x + self.r >= s.x and self.x - self.r <= s.x + s.l and  s.y < tmpg and s.type == "h":
                tmpg = s.y
            
                
        self.g = tmpg
    
    def update(self):
        self.gravity()
        self.y += self.vy
        self.x += self.vx
        
        
            
    
    def display(self):    
        self.update()
        circle(self.x, self.y, self.r * 2)

class Chell(Creature):
    def __init__(self, x, y, r, g):
        Creature.__init__(self, x, y, r, g)
        self.controls = {LEFT:False, RIGHT:False, UP:False}

    
    
        
        
        
    def update(self):
        self.gravity()
        

        if self.controls[LEFT] == True:
            self.vx = -5
            self.direction = LEFT
        elif self.controls[RIGHT] == True:
            self.vx = 5
            self.direction = RIGHT
        else:
            self.vx = 0
        
        if self.controls[UP] == True and self.y+self.r == self.g:
            self.vy = -12
        
        
        
        self.y += self.vy
        self.x += self.vx
        
        for s in game.slist:
            if s.type == "v" and distance(self.x, self.y, s.x, self.y) <= self.r and self.x + self.r >= s.x:
                self.x = s.x + self.r
            elif s.type == "v" and distance(self.x, self.y, s.x, self.y) <= self.r and self.x - self.r <= s.x:
                self.x = s.x - self.r
            
    
        
        
class Surface:
    def __init__(self, x, y, l, type = "h"):
        self.x = x
        self.y = y
        self.l = l
        self.type = type
        
    def display(self):
        stroke(0)
        if self.type == "h":
            strokeWeight(1)
            line(self.x,self.y,self.x+self.l,self.y)
        else:
            strokeWeight(1)
            line(self.x,self.y,self.x,self.y+self.l)

class Portal:
    def __init__(self,x,y,type,nb):
        self.x = x
        self.y = y
        self.type = type
        self.opt = None
        self.nb = nb
    
    def display(self):
        
        if self.nb == 0 and self.type == "h":
            stroke(0,191,255)
            strokeWeight(5)
            line(self.x-15, self.y, self.x+15, self.y)
        elif self.nb == 0 and self.type == "v":
            stroke(0,191,255)
            strokeWeight(5)
            line(self.x,self.y-15,self.x,self.y+15)
        elif self.nb == 1 and self.type == "h":
            stroke(255,165,0)
            strokeWeight(5)
            line(self.x-15, self.y, self.x+15, self.y)
        elif self.nb == 1 and self.type == "v":
            stroke(255,165,0)
            strokeWeight(5)
            line(self.x,self.y-15,self.x,self.y+15)
            

class Game:
    def __init__(self, w, h, g):
        self.w = w
        self.h = h
        self.g = g
        self.chell = Chell(700,650,15,self.g)
        self.slist = []
        self.slist.append(Surface(100,0,700,"v"))
        self.slist.append(Surface(100,100,1280,"h"))
        self.slist.append(Surface(100,700,1280,"h"))
        self.slist.append(Surface(300, 600, 300, "h"))
        self.slist.append(Surface(700, 500, 300, "h"))
        self.portals = []
        self.portals.append(Portal(-1*w, -1*h,"h",0))
        self.portals.append(Portal(-1*w, -1*h,"h",1))
        self.portals[0].opt = self.portals[1]
        self.portals[1].opt = self.portals[0]
                
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
game = Game(1280, 820, 700)
def setup():
    size(game.w, game.h)
    background(255, 255, 255)
def draw():
    background(255, 255, 255)
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
    elif keyCode == RIGHT:
        game.chell.controls[RIGHT] = False
    elif keyCode == UP:
        game.chell.controls[UP] = False   
        
def mouseClicked():
    global PORTALNB
    game.portal_pos()
    for s in game.slist:
        if in_surface(game.portalcoord["x"],game.portalcoord["y"], s):
            game.portals[PORTALNB].type = s.type
    game.portals[PORTALNB].x = game.portalcoord["x"]
    game.portals[PORTALNB].y = game.portalcoord["y"]
    PORTALNB = (PORTALNB + 1)%2
      
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
