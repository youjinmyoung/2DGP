from pico2d import *


class Map:
    def __init__(self):
        self.image = load_image('map.png')

    def draw(self):
        self.image.draw(400, 300)


class Fighter:
    def __init__(self):
        self.image = load_image('fighter.png')

    def draw(self):
        self.image.draw(400,30)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# fill here for boy, grass
running = True

def enter():
    pass


def exit():
    pass


def update():
    pass


def draw():
    pass


def main():
    pass


# fill here


