#This is code for the CP final project - Jackson L
#sources: the ggame documentation by Eric Dennison, and I worked side by side with Nathan (NathanSub on github).
#documentation can be found here: https://ggame.readthedocs.io/en/latest/ggameapi.html#ggame.event.MouseEvent 

from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, Frame
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, 
from random import *

myapp = App()

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
grey = Color(0xCDC0B0, 1.0)
firyred = Color(0xFF3030, 1.0)
purple = Color(0xBF3EFF, 1.0)
gold = Color(0xFFD700, 1.0)
white = Color(0xF8F8FF, 1.0)
violet = Color(0xd147c5, 1.0)
teal = Color(0x95E8C4, 1.0)

thinline = LineStyle(1, black)
noline = LineStyle(0, black)
whiteline = LineStyle(1, white)

class Ball(Sprite):
    b = RectangleAsset(20, 20, noline, white)
    def __init__(self, position):
        super().__init__(Ball.b, position)
        
        if round(randint(0,1)) == 1:
            self.vx = 12
        else:
            self.vx = -12
            
        if round(randint(0,1)) == 1:
            self.vy = 4
        else:
            self.vy = -4

    def step(self):
        self.x += self.vx*0.7
        self.y += self.vy*0.7
        
        if self.y < 1:
            self.vy *= -1
        elif self.y > Pong.height-20:
            self.vy *= -1
            
        if self.x < 0:
            Pong.p2s += 1
            Pong.screen = 2
            self.point.play()
            del Pong.balll[0]
            self.destroy()
        elif self.x > Pong.width-20:
            Pong.p1s += 1
            Pong.screen = 2
            self.point.play()
            del Pong.balll[0]
            self.destroy()
            
        self.pcollide = self.collidingWithSprites(Paddle)
        if len(self.pcollide):
            self.pop.play()
            self.vx = (abs(self.vx)+0.8)
            self.vy = randint(-3,3)
            
        self.pcollide = self.collidingWithSprites(RightPaddle)
        if len(self.pcollide):
            self.pop.play()
            self.vx = ((abs(self.vx)+0.5)*-1)
            self.vy = randint(-3,3)
        
        if len(Pong.balll) == 1:
            Pong.screen = 1
            
class Numbers(Sprite):
    n = ImageAsset("images/numbers4.png",
    Frame(0,0,50,68), 11, 'horizontal')
    def __init__(self, position):
        super().__init__(Numbers.n, position)
        p1s = 0
        self.change = 0
        self.setImage(8)
        Pong.listenKeyEvent("keyup", "o", self.oldnum)
        Pong.listenKeyEvent("keyup", "i", self.newnum)
        self.fxcenter = self.fycenter = 0.5
    
    def step(self, num):
        self.setImage(num)
        if Pong.p1s == 10:
            Pong.p1s = 0
        if Pong.p2s == 10:
            Pong.p2s = 0

    def oldnum(self, event):
        Pong.p1s += 1

    def newnum(self, event):
        Pong.p2s += 1
        
class Leftnum(Numbers):
    def step(self, num):
        self.setImage(num)

class Paddle(Sprite):
    p = RectangleAsset(10, 40, noline, white)
    def __init__(self, position):
        super().__init__(Paddle.p, position)
        self.vy = 0
        self.vy2 = 0
        for i in keys:
            Pong.listenKeyEvent("keydown", i, self.press)
            Pong.listenKeyEvent("keyup", i, self.stop)
            
    def press(self, event):
        if event.key == "up arrow":
            self.vy2 = -5
        elif event.key == "down arrow":
            self.vy2 = 5
        elif event.key == "w":
            self.vy = -5
        elif event.key == "s":
            self.vy = 5

    def stop(self, event):
        if event.key == "up arrow":
            self.vy2 = 0
        elif event.key == "down arrow":
            self.vy2 = 0
        else:
            self.vy = 0

    def step(self):
        self.y += self.vy
        if self.y > Pong.height-20:
            self.y = Pong.height-20
        elif self.y < 0:
            self.y = 0

class RightPaddle(Paddle):
    def step(self):
        self.y += self.vy2
        if self.y > Pong.height-20:
            self.y = Pong.height-20
        elif self.y < 0:
            self.y = 0

class StartScreen(Sprite):
    s = ImageAsset("images/play.png")
    def __init__(self, position):
        super().__init__(StartScreen.s, position)
        self.flash = 0
        self.on = 0
        self.fxcenter = self.fycenter = 0.5

    def step(self):
        if self.flash == 35:
            if self.on == 0 and Pong.screen == 0:
                self.y = 200
                self.x = Pong.width/2
                self.on = 1
            else:
                self.y = -100
                self. on = 0

            self.flash = 0
        self.flash += 1

class Serve(Sprite):
    r = ImageAsset("images/again.png")
    def __init__(self, position):
        super().__init__(Serve.r, position)
        self.fxcenter = self.fycenter = 0.5
        self.flash = 0
        self.on = 0

    def step(self):
        if self.flash == 35:
            if self.on == 0 and Pong.screen == 2:
                self.y = 200
                #self.x = Pong.width/2
                self.on = 1
            else:
                self.y = -100
                self. on = 0
            self.flash = 0
        self.flash += 1

class Win(Sprite):
    w = ImageAsset("images/wins.png",
    Frame(0,0,600,80), 2, 'horizontal')
    def __init__(self, position):
        super().__init__(Win.w, position)
        self.fxcenter = self.fycenter = 0.5
        self.image = 0 
    def step(self):
        if Pong.p1s == 7 or Pong.p2s == 7:
            self.victory.play()
            Pong.balll.append('game over')
            Pong.screen = 3
            self.y = 300
            if Pong.p1s == 7:
                self.setImage(2)
            else:
                self.setImage(1)
        
class Pong(App):
    screen = 0
    p1s = 8
    p2s = 8
    balll = []
    def __init__(self):
        super().__init__()
        bg_main = RectangleAsset(self.width, self.height, noline, black)
        bg_center =  RectangleAsset(5, round(self.height/40), noline, white)
        bg_top = RectangleAsset(self.width, 20, noline, white)
        bg = Sprite(bg_main, (0,0))
        Numbers((self.width/2-100, 100))
        Leftnum((self.width/2+100, 100))
        StartScreen((self.width/2, -200))
        Serve((self.width/2, -200))
        Win((self.width/2, -100))
        Paddle((50,self.height/2))
        RightPaddle((self.width-50,self.height/2))
        for i in range(round(self.height/20)):
            bg = Sprite(bg_center, (self.width/2-5, i*35))

        Pong.listenKeyEvent("keydown", "space", self.placeball)
    
    def placeball(self, event):
        if len(self.balll) == 0:
            self.balll.append(Ball((self.width/2, randint(100, self.height-75))))
        
    def step(self):
        for n in self.getSpritesbyClass(Numbers):
            n.step(self.p1s)
            
        for n in self.getSpritesbyClass(Leftnum):
            n.step(self.p2s)
            
        for p in self.getSpritesbyClass(Paddle):
            p.step()
        
        for p in self.getSpritesbyClass(RightPaddle):
            p.step()
        
        for s in self.getSpritesbyClass(Serve):
            s.scale = 0.5
            s.step()
            
        for s in self.getSpritesbyClass(StartScreen):
            s.scale = 0.5
            s.step()
        
        for w in self.getSpritesbyClass(Win):
            w.step()

        if len(self.balll) == 1:
            for b in self.getSpritesbyClass(Ball):
                b.step()

myApp = Pong()
myApp.run()