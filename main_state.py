import random
import json
import os

from pico2d import *

import game_framework
import title_state

name = "MainState"

fighter = None
map = None

class map:
    def __init__(self):
        self.image = load_image('map.png')

    def draw(self):
        self.image.draw(400,300)


class fighter:
    def __init__(self):
        self.image = load_image('fighter.png')

    def draw(self):
        self.image.draw(400, 300)


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
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            # p key go to pause_state
            game_framework.push_state(pause_state)
    pass