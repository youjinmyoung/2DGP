from pico2d import *
import random


class Enemy:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 5.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 2

    image = None

    LEFT_FLY, RIGHT_FLY = 0, 1

    def __init__(self):
        self.x, self.y = random.randint(1,790), 500
        self.frame = random.randint(0, 1)
        self.total_frames = 0.0
        self.dir = 1
        self.state = self.RIGHT_FLY

        if Enemy.image == None:
            Enemy.image = load_image('enemy1(200x100).png')


    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        self.total_frames += Enemy.FRAMES_PER_ACTION * Enemy.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 2
        self.x += (self.dir * distance)
        if self.x >= 110:
            self.dir = -1
        elif self.x <= 90:
            self.dir = 1


    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())