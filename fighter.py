from pico2d import *


class Fighter:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    DEATH_TIME_PER_ACTION = 1
    DEATH_ACTION_PER_TIME = 1.0 / DEATH_TIME_PER_ACTION
    DEATH_FRAMES_PER_ACTION = 2

    image = None
    death_image = None
    death_sound = None
    LEFT_FLY, RIGHT_FLY, STOP = 0, 1 ,2

    def __init__(self):
        self.x, self.y = 400, 50
        self.dir = 0
        self.state = self.STOP
        self.launch = False
        self.death = False
        self.death_frame = 0.0
        self.death_total_frame = 0.0
        Fighter.image = load_image('resource/fighter/fighter.png')
        Fighter.death_image = load_image('resource/fighter/fighter_D.png')
        if self.death_sound == None:
            Fighter.death_sound = load_wav('wav_sounds/explosion.wav')
            Fighter.death_sound.set_volume(32)

    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.death_total_frame += Fighter.DEATH_FRAMES_PER_ACTION * Fighter.DEATH_ACTION_PER_TIME * frame_time
        self.death_frame = int(self.death_total_frame) % 4

        distance = Fighter.RUN_SPEED_PPS * frame_time
        self.x += (self.dir * distance)
        self.x = clamp(50, self.x, 750)



    def draw(self):
        if self.death == False:
            self.image.draw(self.x, self.y)
        elif self.death == True:
            self.death_image.clip_draw(self.death_frame * 100, 0, 100, 100, self.x, self.y)
            if self.death_frame == 3:
                self.death = False
                self.x = 400
                self.y = 50


    def die(self):
        self.death = True
        self.death_sound.play()

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x -30, self.y -30, self.x + 30, self.y + 30
        pass

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_FLY, self.STOP):
                self.state = self.LEFT_FLY
                self.dir = -1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.LEFT_FLY, self.STOP):
                self.state = self.RIGHT_FLY
                self.dir = 1
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_FLY,):
                self.state = self.STOP
                self.dir = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_FLY,):
                self.state = self.STOP
                self.dir = 0