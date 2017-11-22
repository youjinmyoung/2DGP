from pico2d import *

import game_framework
import title_state
import pause_state


from map import Map
from fighter import Fighter
from enemy import Enemy
from missile import Missile

name = "MainState"

map = None
fighter = None
enemy = None
missile = None
enemys = None

def create_world():
    global map, fighter, enemys, missile
    map = Map()
    fighter = Fighter()
    enemys = [Enemy() for i in range(3)]
    missile = Missile()
    pass


def destroy_world():
    global map, fighter, enemys, missile

    del(map)
    del(fighter)
    del(enemys)
    del(missile)

def enter():
    #open_canvas()
    #game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    #close_canvas()


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global missile
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)
        else:
            fighter.handle_event(event)
            missile.handle_event(event)





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
    for enemy in enemys:
        enemy.update(frame_time)
    missile.update(frame_time, fighter.x)

    #if collide(enemy, missile):
      #  enemy.remove(enemy)
    pass



def draw(frame_time):
    clear_canvas()
    map.draw()
    fighter.draw()
    missile.draw()
    for enemy in enemys:
        enemy.draw()

    fighter.draw_bb()
    missile.draw_bb()
    for enemy in enemys:
        enemy.draw_bb()
    pass

    update_canvas()






