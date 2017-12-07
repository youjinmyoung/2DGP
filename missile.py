from pico2d import *

class FighterMissile:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 35.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None
    missile_sound = None

    def __init__(self):
        self.x, self.y = -30, -30
        self.dir = 1
        self.missile_ready = False
        self.launch = False
        if FighterMissile.image == None:
            FighterMissile.image = load_image('resource/mis1.png')
        if FighterMissile.missile_sound == None:
            FighterMissile.missile_sound = load_music('sounds/shot.mp3')
            FighterMissile.missile_sound.set_volume(32)

    def update(self, frame_time, fighter_x, fighter_y):
        if self.missile_ready == True:
            if self.launch == True:
                self.x = fighter_x
                self.y = fighter_y + 30
                self.missile_sound.play()
                self.launch = False
            if self.y >= 650:
                self.missile_ready = False

            distance = self.RUN_SPEED_PPS * self.dir * frame_time
            self.y +=  distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.missile_ready == False:
                self.missile_ready= True
                self.launch = True

        pass

    def stop(self):
        self.missile_ready = False
        self.y = -30
        pass

    def get_bb(self):
        return self.x - 10, self.y - 15, self.x + 8, self.y + 15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class EnemyMissile:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 30.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None

    def __init__(self):
        self.x, self.y = 100, 500
        self.dir = -1
        self.missile_ready = False
        self.launch = False
        self.launch_time = 0
        if EnemyMissile.image == None:
            EnemyMissile.image = load_image('resource/enemy/enemy_missile.png')


    def update(self, frame_time, enemy_x, enemy_y):
        self.launch_time += frame_time * 10
        print(self.launch_time)
        if self. missile_ready == True:
            if self.launch == True:
                self.x = enemy_x
                self.y = enemy_y - 30
                self.launch = False
            if self.y <= 0:
                self.missile_ready = False
        if self.launch_time >= 20:
            if self.missile_ready == False:
                self.missile_ready = True
                self.launch = True

            distance = self.RUN_SPEED_PPS * self.dir * frame_time
            self.y += distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def handle_event(self, event):
        pass

    def stop(self):
        self.missile_ready = False
        self.y = -30
        pass

    def get_bb(self):
        return self.x - 10, self.y - 15, self.x + 8, self.y + 15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())