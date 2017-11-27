from pico2d import *


class Map:
    PIXEL_PER_METER = (10.0 / 0.3)
    SCROLL_SPEED_KMPH = 10.0
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self, w, h):
        self.image = load_image('resource/map.png')
        self.speed = 0
        self.down = 0
        self.map_width = w
        self.map_heigh = h


    def draw(self):
        y = int(self.down)
        h = min(self.image.h - y, self.map_heigh)
        self.image.clip_draw_to_origin(0, y, self.map_width, h, 0, 0)
        self.image.clip_draw_to_origin(0, 0, self.map_width, self.map_heigh -h, 0, h)

    def update(self,frame_time):
        self.down = (self.down + frame_time * self.speed) % self.image.h
        self.speed = Map.SCROLL_SPEED_PPS


