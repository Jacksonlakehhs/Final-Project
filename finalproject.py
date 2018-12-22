from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, Frame

# add your code here \/  \/  \/
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, SoundAsset

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

class Paddle(Sprite):
    paddle = ImageAsset("images/7T12W105.jpg")

    def __init__(self, position):
        super().__init__(Paddle.paddle, position)
        self.vx = 1
        self.vy = 1
        self.center = (0.5, 0.5)

        Pong.listenKeyEvent("keydown", "right arrow", self.rightarrowKey)
        Pong.listenKeyEvent('keydown', "left arrow", self.leftarrowKey)
        Pong.listenKeyEvent('keydown', "up arrow", self.uparrowKey)
        Pong.listenKeyEvent('keydown', "down arrow", self.downarrowKey)
        
                
    def rightarrowKey(self, event):
        self.vx+=.2
        
    def leftarrowKey(self, event):
        self.vx+=-.2
        
    def uparrowKey(self, event):
        self.vy+=-.2
        
    def downarrowKey(self, event):
        self.vy+=.2


    def step(self):
        self.x += self.vx
        self.y += self.vy


class Pong(App):
    def __init__(self):
        super().__init__()
        bg_asset = ImageAsset("images/istockphoto-114445289-612x612.jpg")
        bg = Sprite(bg_asset, (-100, -115))
        bg.scale = 2
        self.paddle1 = Paddle((500, 30))
    

myapp = Pong()
myapp.run()