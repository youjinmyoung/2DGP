from pico2d import *

class P_Missile:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 35.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None

    def __init__(self):
        self.x, self.y = -30, -30
        self.dir = 1
        self.missile_on = False
        self.launch = False
        if P_Missile.image == None:
            P_Missile.image = load_image('resource/mis1.png')

    def update(self, frame_time, fighter_x):
        if self.missile_on == True:
            if self.launch == True:
                self.x = fighter_x
                self.launch = False
            if self.y >= 650:
                self.missile_on = False

            distance = self.RUN_SPEED_PPS * frame_time
            self.y +=  distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.missile_on == False:
                self.y = 80
                self.missile_on= True
                self.launch = True

        pass

    def stop(self):
        self.missile_on = False
        self.y = -30
        pass

    def get_bb(self):
        return self.x - 10, self.y - 15, self.x + 8, self.y + 15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class E_missile:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 30.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None

    def __init__(self):
        self.x, self.y = -30, -30
        self.dir = -1
        self.missile_on = False
        self.launch = False
        if P_Missile.image == None:
            P_Missile.image = load_image('resource/mis1.png')

    def update(self, frame_time, enemy_x, enemy_y):
        if self.missile_on == True:
            if self.launch == True:
                self.x = enemy_x
                self.y = enemy_y
                self.launch = False
            if self.y <= -50:
                self.missile_on = False

            distance = self.RUN_SPEED_PPS * frame_time
            self.y -= distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def handle_event(self, event):
        pass

    def stop(self):
        self.missile_on = False
        self.y = -30
        pass

    def get_bb(self):
        return self.x - 10, self.y - 15, self.x + 8, self.y + 15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())