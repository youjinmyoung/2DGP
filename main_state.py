import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state

name = "MainState"

fighter = None
map = None
left_pressed = False
right_pressed = False

class Map:
    def __init__(self):
        self.image = load_image('map.png')

    def draw(self):
        self.image.draw(400,300)


class Fighter:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    global left_pressed, right_pressed
    def __init__(self):
        self.image = load_image('fighter.png')
        self.x, self.y = 400, 40

    def update(self):
        if(left_pressed):
            self.x = max(0, self.x - 2)
        elif(right_pressed):
            self.x = min(800, self.x + 2)

        pass

    def draw(self):
        self.image.draw(self.x, self.y)


def enter():
    global fighter, map
    fighter = Fighter()
    map = Map()


def exit():
    global fighter, map
    del(fighter)
    del(map)

def pause():
    pass


def resume():
    pass


def handle_events():
    global left_pressed, right_pressed
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            # p key go to pause_state
            game_framework.push_state(pause_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            left_pressed = True
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            left_pressed = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            right_pressed = True
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            right_pressed = False
    pass


def update():
    fighter.update()


def draw_state():
    map.draw()
    fighter.draw()


def draw():
    clear_canvas()
    draw_state()
    update_canvas()