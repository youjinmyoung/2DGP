from pico2d import *

import game_framework

from map import Map
from fighter import Fighter

name = "MainState"

map = None
fighter = None


def create_world():
    global map, fighter
    map = Map()
    fighter = Fighter()

    pass


def destroy_world():
    global map, fighter

    del(map)
    del(fighter)


def enter():
    open_canvas()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                fighter.handle_event(event)




def collide(a, b):
    # fill here
    global check
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False


    return True
    pass

def update(frame_time):
    fighter.update(frame_time)
    pass



def draw(frame_time):
    clear_canvas()
    map.draw()
    fighter.draw()

    pass

    update_canvas()






