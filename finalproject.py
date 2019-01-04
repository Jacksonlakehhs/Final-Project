'''
Jackson Lake
Sources:
https://ggame-dev.readthedocs.io/en/latest/_modules/ggame/asset.html#PolygonAsset
'''
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
from ggame import ImageAsset, Frame, Sound, SoundAsset, TextAsset

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

thinline = LineStyle(1, black)
noline = LineStyle(0, black)
whiteline = LineStyle(1, white)


class Ball(Sprite):
    ball = CircleAsset(100, whiteline, white)
    
    def __init__(self, position):
        super().__init__(Ball.ball, position)
        self.vx = 3
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
    
        if collisionright:
            self.vx = -3
    

class Paddle1(Sprite):
    paddle1 = RectangleAsset(50, 500, thinline, red)
    
    def __init__(self, position):
        super().__init__(Paddle1.paddle1, position)
        self.vx = 0
        self.vy = 0
        self.center = (0.5, 0.5)
        self.scale = 0.2
        
        Pong.listenKeyEvent('keydown', "w", self.uparrowKey)
        Pong.listenKeyEvent('keydown', "s", self.downarrowKey)
        
    def uparrowKey(self, event):
        if self.y >= 120:
            self.y -= 5
    
    def downarrowKey(self, event):
        if self.y <= 420:
            self.y+=5

    def step(self):
        self.y += self.vy
    

class Paddle2(Sprite):
    paddle2 = RectangleAsset(50, 500, thinline, red)
    
    def __init__(self, position):
        super().__init__(Paddle2.paddle2, position)
        self.vx = 0
        self.vy = 0
        self.center = (0.5, 0.5)
        self.scale = 0.2
        
        Pong.listenKeyEvent('keydown', "up arrow", self.uparrowKey)
        Pong.listenKeyEvent('keydown', "down arrow", self.downarrowKey)
        
    def uparrowKey(self, event):
        if self.y >= 120:
            self.y -= 5
    
    def downarrowKey(self, event):
        if self.y <= 420:
            self.y+=5

    def step(self):
        self.y += self.vy
    
        
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
        
        self.borderleft = Borderleft((80, 265))

        self.borderright = Borderright((1100, 265))
        
        self.bordertop = Bordertop((515, 60))
        
        self.borderbottom = Borderbottom ((515, 470))
    
    def step(self):
        if self.paddle1:
            self.paddle1.step()
            
        if self.paddle2:
            self.paddle2.step()
    
    def step(self):
        if self.ball:
            self.ball.step()
            
    

myapp = Pong()

myapp.run()