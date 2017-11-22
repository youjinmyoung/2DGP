from pico2d import *
import random

class Missile:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 30.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None

    def __init__(self):
        self.x, self.y = -30, -30
        self.launch = False
        self.launch_start = False

        self.launch_dir = -1
        if Missile.image == None:
            Missile.image = load_image('mis1.png')

    def update(self,frame_time, fighter_x):
        if self.launch == True:
            if self.launch_start == True:
                self.x = fighter_x
                self.launch_start = False
            if self.y >= 630:
                self.y = self.launch_dir * 30
                self.launch = False

            distance = self.RUN_SPEED_PPS * frame_time
            self.y += distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.launch == False:
                self.y = 50
                self.launch = True
                self.launch_start = True

    def stop(self):
        self.launch = False
        self.y = -40

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
