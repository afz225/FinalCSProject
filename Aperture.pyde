


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
        
    
        
        
        
        
class Surface:
    def __init__(self, x, y, l, type = "h"):
        self.x = x
        self.y = y
        self.l = l
        self.type = type
        
    def display(self):
        stroke(0)
        if self.type == "h":
            line(self.x,self.y,self.x+self.l,self.y)
        else:
            line(self.x,self.y,self.x,self.y+self.l)

class Game:
    def __init__(self, w, h, g):
        self.w = w
        self.h = h
        self.g = g
        self.chell = Chell(15,15,15,self.g)
        self.slist = []
        self.slist.append(Surface(100,0,700,"v"))
        self.slist.append(Surface(100,100,1280,"h"))
                
        self.portalcoord = {"x":0,"y":0}
    
    
    def portal_pos(self):
        for s in self.slist:
            if s.type == "v":
                Y = ((((self.h-mouseY)-(self.h-self.chell.y))/(mouseX - self.chell.x))*(s.x - self.chell.x)) + (self.h - self.chell.y)
                Y = self.h - Y
                if in_surface(s.x,Y,s):
                    self.portalcoord["x"] = s.x
                    self.portalcoord["y"] = Y
            else:
                X = (((self.h-s.y)-(self.h-self.chell.y))/((self.h-mouseY)-(self.h-self.chell.y)))*(mouseX-self.chell.x) + self.chell.x
                if in_surface(X,s.y,s):
                    self.portalcoord["x"] = X
                    self.portalcoord["y"] = s.y
    # def portal_pos(self, tx, ty):
    #     if in_surface(tx,ty):
    #         self.portalcoord["x"] = tx
    #         self.portalcoord["y"] = ty
    #         return true
        
    #     if mouseX > self.chell.x:
    #         ntx,nty = tx+1, ty + ((mouseY-self.chell.y)/(mouseX-self.chell.x))
        
    #     elif mouseX < self.chell.x:
    #         ntx,nty = tx-1, ty + ((mouseY-self.chell.y)/(mouseX-self.chell.x))
    #     elif mouseX == self.chell.x and mouseY > self.chell.y:
    #         ntx,nty = tx, ty + 1
    #     else:
    #         ntx,nty = tx, ty - 1
            
    #     if self.portal_pos(ntx,nty):
    #         return True
        
    #     self.portalcoord["x"] = ""
    #     self.portalcoord["y"] = ""
    
    
    def display(self):
        self.chell.display()
        
        
        for s in self.slist:
            s.display()
        
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
     
    game.portal_pos()
    print(str(game.portalcoord["x"]) +","+ str(game.portalcoord["y"]))  
def in_surface(n,m,s):

    if s.x <= n and n <= (s.x + s.l) and s.y == m and s.type == "h":
        return True
    elif ((s.y <= m) and (m <= (s.y + s.l)) and (s.x == n) and (s.type == "v")):
        return True
    
    return False
