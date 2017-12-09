from pico2d import *
import random


class GreenEnemy:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 15.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 1

    DEAD_TIME_PER_ACTION = 1
    DEAD_ACTION_PER_TIME = 1.0 / DEAD_TIME_PER_ACTION
    DEAD_FRAMES_PER_ACTION = 4

    image = None
    twist_image = None
    death_image = None
    death_sound = None
    LEFT_FLY, RIGHT_FLY = 0, 1

    def __init__(self):
        self.x, self.y = 0, 0
        self.frame = 0
        self.death_frame = 0
        self.total_frames = 0.0
        self.death_total_frames = 0.0
        self.dir = 1
        self.state = 0
        self.death = False

        self.image = load_image('resource/enemy/green_enemy.png')
        self.death_image = load_image('resource/enemy/dead.png')
        if self.twist_image == None:
            self.twist_image = load_image('resource/enemy/green_enemy_twist.png')
        if GreenEnemy.death_sound == None:
            GreenEnemy.death_sound = load_music('wav_sounds/explosion.wav')
            GreenEnemy.death_sound.set_volume(32)


    def update(self, frame_time):
        self.total_frames += GreenEnemy.FRAMES_PER_ACTION * GreenEnemy.ACTION_PER_TIME * frame_time
        self.death_total_frames += GreenEnemy.DEAD_FRAMES_PER_ACTION * GreenEnemy.DEAD_ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 2
        self.death_frame = int(self.death_total_frames) % 4
        distance = self.RUN_SPEED_PPS * self.dir * frame_time
        self.y -= distance
        if self.y <= 450:
            self.RUN_SPEED_PPS = 0

    def die(self):
        self.death = True
        self.death_sound.play()

    def draw(self):
        if self.y >= 450:
            self.twist_image.clip_draw(self.frame * 80, 0, 80, 80, self.x, self.y)
        if self.death == False and self.y <= 450:
            self.image.clip_draw(self.frame * 80, 0, 80, 80, self.x, self.y)
        elif self.death == True:
            self.death_image.clip_draw(self.death_frame * 70, 0, 60, 70, self.x, self.y)
            if self.death_frame == 3:
                self.frame = -1
                self.death = False
                self.x, self.y = -100, -100

    def locate(self):
        return self.x, self.y

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 35

    def draw_bb(self):
        draw_rectangle(*self.get_bb())



