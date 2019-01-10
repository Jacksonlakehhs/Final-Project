'''
Jackson Lake
Sources:
https://ggame-dev.readthedocs.io/en/latest/_modules/ggame/asset.html#PolygonAsset
https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python
Eric Dennison
'''
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
from ggame import ImageAsset, Frame, Sound, SoundAsset, TextAsset
import random

white = Color(0xffffff, 1.0)
clear = Color(0xffffff, 0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
eye = Color(0xdee5ef, 1.0)
sand = Color(0xefe49b, 1.0)
meadowgreen = Color(0x8ed334, 1.0)
orange = Color(0xe59e19, 1.0)
yellow = Color(0xccff00, 1.0)

thinline = LineStyle(1, black)
noline = LineStyle(0, black)
whiteline = LineStyle(1, white)


class Ball(Sprite):
    ball = EllipseAsset(100, 100, whiteline, yellow)
    
    def __init__(self, position):
        super().__init__(Ball.ball, position)
        self.vx = 20
        self.vy = 0
        self.thrust = 0
        self.thrustframe = 1
        self.center = (0.5, 0.5)
        self.scale = 0.2
        
    def step(self):
        self.x += self.vx * 0.7
        self.y += self.vy * 0.7
        
        collisionleft = self.collidingWith(myapp.borderleft) 
        collisionright = self.collidingWith(myapp.borderright)
        hitspaddle2 = self.collidingWith(myapp.paddle2)
        hitspaddle1 = self.collidingWith(myapp.paddle1)
        hitsbordertop = self.collidingWith(myapp.bordertop)
        hitsborderbott = self.collidingWith(myapp.borderbottom)
        
        rand = random.randint(0, 8)
    
        if hitspaddle2:
            self.vx = -20
            if rand == 0:
                self.vy = 3
            elif rand == 1:
                self.vy = -3
            elif rand == 2:
                self.vy = 6
            elif rand == 3:
                self.vy = -6
        
        elif hitspaddle1:
            self.vx = 20
            if rand == 0:
                self.vy = 3
            elif rand == 1:
                self.vy = -3
            elif rand == 2:
                self.vy = 7
            elif rand == 3:
                self.vy = -7
        
        elif collisionright:
            self.vx = 0
            self.visible = False
        
        elif collisionleft:
            self.vx = 0
            self.visible = False
        
        elif hitsbordertop:
            self.vy = self.vy*-1
        
        elif hitsborderbott:
            self.vy = self.vy*-1

class Paddle1(Sprite):
    paddle1 = RectangleAsset(60, 333, thinline, blue)
    
    def __init__(self, position):
        super().__init__(Paddle1.paddle1, position)
        self.vx = 0
        self.vy = 0
        self.center = (0.5, 0.5)
        self.scale = 0.2
        self.downpressed = False
        self.uppressed =  False
        
        Pong.listenKeyEvent('keydown', "w", self.uparrowKey)
        Pong.listenKeyEvent('keyup', "w", self.uparrowKeyisUp)
        Pong.listenKeyEvent('keyup', "s", self.downarrowKeyisUp)
        Pong.listenKeyEvent('keydown', "s", self.downarrowKey)
        
    def uparrowKeyisUp(self, event):
        self.uppressed = False
    
    def downarrowKeyisUp(self, event):
        self.downpressed = False

    def uparrowKey(self, event):
        self.uppressed = True
    
    def downarrowKey(self, event):
        self.downpressed = True


    def step(self):
        if self.uppressed and self.y >= 100:
            self.y -= 10
        if self.downpressed and self.y <= 440:
            self.y += 10
    

class Paddle2(Sprite):
    paddle2 = RectangleAsset(60, 333, thinline, red)
    
    def __init__(self, position):
        super().__init__(Paddle2.paddle2, position)
        self.vx = 0
        self.vy = 0
        self.center = (0.5, 0.5)
        self.scale = 0.2
        self.downpressed = False
        self.uppressed =  False
        
        Pong.listenKeyEvent('keydown', "up arrow", self.uparrowKey)
        Pong.listenKeyEvent('keyup', "up arrow", self.uparrowKeyisUp)
        Pong.listenKeyEvent('keyup', "down arrow", self.downarrowKeyisUp)
        Pong.listenKeyEvent('keydown', "down arrow", self.downarrowKey)
        
    def uparrowKeyisUp(self, event):
        self.uppressed = False
    
    def downarrowKeyisUp(self, event):
        self.downpressed = False

    def uparrowKey(self, event):
        self.uppressed = True
    
    def downarrowKey(self, event):
        self.downpressed = True


    def step(self):
        if self.uppressed and self.y >= 100:
            self.y -= 10
        if self.downpressed and self.y <= 440:
            self.y += 10
    

class Borderleft(Sprite):
    borderleft = RectangleAsset(100, 2000, whiteline, blue)

    def __init__(self, position):
        super().__init__(Borderleft.borderleft, position)
        self.vx = 1
        self.vy = 1
        self.center = (0.5, 0.5)
        self.scale = 0.2
        self.visible = False

class Borderright(Sprite):
    borderright = RectangleAsset(100, 2000, whiteline, blue)

    def __init__(self, position):
        super().__init__(Borderright.borderright, position)
        self.vx = 1
        self.vy = 1
        self.center = (0.5, 0.5)
        self.scale = 0.2
        self.visible = False

class Bordertop(Sprite):
    bordertop = RectangleAsset(4200, 100, whiteline, green)

    def __init__(self, position):
        super().__init__(Bordertop.bordertop, position)
        self.vx = 1
        self.vy = 1
        self.center = (0.5, 0.5)
        self.scale = 0.2
        self.visible = False
        
class Borderbottom(Sprite):
    borderbottom = RectangleAsset(4200, 100, whiteline, green)

    def __init__(self, position):
        super().__init__(Borderbottom.borderbottom, position)
        self.vx = 1
        self.vy = 1
        self.center = (0.5, 0.5)
        self.scale = 0.2
        self.visible = False


class Pong(App):
    def __init__(self):
        super().__init__()
        bg_asset = ImageAsset("images/istockphoto-114445289-612x612.jpg")
        bg = Sprite(bg_asset, (-100, -115))
        bg.scale = 2
        
        self.ball = Ball((515, 265))
        
        self.paddle1 = Paddle1((97, 265))
        
        self.paddle2 = Paddle2((935, 265))
        
        self.borderleft = Borderleft((0, 265))

        self.borderright = Borderright((1100, 265))
        
        self.bordertop = Bordertop((515, 60))
        
        self.borderbottom = Borderbottom((515, 470))
        

    def step(self):
        if self.ball:
            self.ball.step()

        if self.paddle1:
            self.paddle1.step()
            
        if self.paddle2:
            self.paddle2.step()

    

myapp = Pong()

myapp.run()