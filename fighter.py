from pico2d import *


class Fighter:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None

    LEFT_FLY, RIGHT_FLY, STOP = 0, 1 ,2

    def __init__(self):
        self.x, self.y = 400, 50
        self.dir = 0
        self.state = self.STOP
        self.launch = False
        if Fighter.image == None:
            Fighter.image = load_image('resource/fighter/fighter.png')


    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        distance = Fighter.RUN_SPEED_PPS * frame_time
        self.x += (self.dir * distance)
        self.x = clamp(0, self.x, 800)



    def draw(self):
        self.image.draw(self.x, self.y)

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