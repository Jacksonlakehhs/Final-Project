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


class Pong(App):
    def __init__(self):
        super().__init__()
        bg_asset = ImageAsset("images/istockphoto-114445289-612x612.jpg")
        bg = Sprite(bg_asset, (0, 0))
        bg.scale = 2
        
        


myapp = Pong()
myapp.run()