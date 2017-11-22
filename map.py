from pico2d import *


class Map:
    def __init__(self):
        self.image = load_image('map.png')
        self.x = 400
        self.y = 300

    def draw(self):
        self.image.draw(400, 300)



