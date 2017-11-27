from pico2d import *
import random

class Enemy3:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 5.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 1

    image = None
    dead_image = None
    LEFT_FLY, RIGHT_FLY = 0, 1

    def __init__(self):
        self.x, self.y = 0, 0
        self.frame = random.randint(0, 1)
        self.dead_frame = (0, 4)
        self.total_frames = 0.0
        self.dir = 0
        self.state = 0
        self.dead = False

        self.image = load_image('resource/enemy3.png')
        self.dead_image = load_image('resource/enemy_D.png')


    def update(self, frame_time):
        self.total_frames += Enemy3.FRAMES_PER_ACTION * Enemy3.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 2
        self.dead_frame =int(self.total_frames + 1) % 4

    def dead(self):
        self.dead = True

    def stop(self):
        self.dead = True

        pass
    def draw(self):
        if self.dead == False:
            self.image.clip_draw(self.frame * 80, 0, 80, 80, self.x, self.y)
        elif self.dead == True:
            self.dead_image.clip_draw(self.dead_frame * 70, 0, 60, 70, self.x,self.y)
            if self.dead_frame == 3:
                self.frame = -1
                self.dead = False
                self.x, self.y = -100, -100


    def get_bb(self):
        return self.x - 25, self.y - 15, self.x + 25, self.y + 25

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
