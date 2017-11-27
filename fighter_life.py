from pico2d import*

class Fighter_life:
    image = None

    def __init__(self):
        # 여기서부터 내가 코딩
        self.draw_x, self.draw_y = 50, 50
        self.life = 0

        if self.image == None:
            self.image = load_image('resource/life.png')

    def update(self,frame_time):
        pass

    def draw(self):
        self.image.draw(self.draw_x, self.draw_y)