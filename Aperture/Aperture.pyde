


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
        
        
        


class Game:
    def __init__(self, w, h, g):
        self.w = w
        self.h = h
        self.g = g
        self.chell = Chell(15,15,15,self.g)
    
    def display(self):
        self.chell.display()
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
