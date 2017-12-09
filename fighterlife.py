from pico2d import*

class FighterLife:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.life = 0

        if self.image == None:
            self.image = load_image('resource/fighter/life.png')

    def update(self,frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)