from pico2d import *

import game_framework
import title_state
import pause_state


from map import Map
from fighter import Fighter
from enemy1 import Enemy1
from enemy2 import Enemy2
from enemy3 import Enemy3
from missile import P_Missile, E_missile
from score import Score
from score2 import Score2
from fighter_life import Fighter_life
name = "MainState"

map = None
fighter = None
p_missile = None
e_missile = None
enemy1 = None
enemy2 = None
enemy3 = None
enemies1 = None
enemies2 = None
enemies3 = None
score = 0
score2 = None
score_data = None
draw_score = None
fighter_life = None

enemies1_data_file = open('enemy1.txt','r')
enemies1_data = json.load(enemies1_data_file)
enemies1_data_file.close()

enemies2_data_file = open('enemy2.txt','r')
enemies2_data = json.load(enemies2_data_file)
enemies2_data_file.close()

enemies3_data_file = open('enemy3.txt','r')
enemies3_data = json.load(enemies3_data_file)
enemies3_data_file.close()


def create_enemy1():
    enemies1 = []
    for name in enemies1_data:
        enemy1 = Enemy1()
        enemy1.name = name
        enemy1.x = enemies1_data[name]['x']
        enemy1.y = enemies1_data[name]['y']
        enemies1.append(enemy1)
    return enemies1

def create_enemy2():
    enemies2 = []
    for name in enemies2_data:
        enemy2 = Enemy2()
        enemy2.name = name
        enemy2.x = enemies2_data[name]['x']
        enemy2.y = enemies2_data[name]['y']
        enemies2.append(enemy2)
    return enemies2

def create_enemy3():
    enemies3 = []
    for name in enemies3_data:
        enemy3 = Enemy3()
        enemy3.name = name
        enemy3.x = enemies3_data[name]['x']
        enemy3.y = enemies3_data[name]['y']
        enemies2.append(enemy3)
    return enemies3

def create_world():
    global map, fighter, enemies1, p_missile, enemies2, enemies3, e_missile
    global draw_score, fighter_life, score2
    map = Map(800,600)

    draw_score = Score()
    score2 = Score2()
    fighter_life = Fighter_life()

    fighter = Fighter()
    enemies1 = create_enemy1()
    enemies2 = create_enemy2()
    enemies3 = create_enemy3()
    p_missile = P_Missile()
    e_missile = [E_missile() for i in range(4)]
    pass


def destroy_world():
    global map, fighter, enemies1, p_missile, enemies2, enemies3, e_missile
    global draw_score, fighter_life, score2
    for missile in e_missile:
        if missile.missile_on == True:
            missile.missile_on = False

    del(map)
    del(fighter)
    del(enemies1)
    del(enemies2)
    del(enemies3)
    del(p_missile)
    del(e_missile)
    del(draw_score)
    del(fighter_life)
    del(score2)

def enter():
    #open_canvas()
    #game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    #close_canvas()

def save_score():
    global score_data, score

    f = open('resource/data_file.txt','r')
    score_data = json.load(f)
    f.close()

    score_data.append({'score':score})

    f = open('resource/data_file.txt', 'w')
    json.dump(score_data, f)
    f.close()

def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global p_missile
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
            p_missile.handle_event(event)






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
    global score, draw_score
    fighter.update(frame_time)
    map.update(frame_time)
    p_missile.update(frame_time, fighter.x)
    draw_score.update(frame_time, score)

    for missile in e_missile:
        if missile.missile_on == True:
            missile.update(frame_time, enemies3.x, enemies3.y)


    for enemy1 in enemies1:
        enemy1.update(frame_time)
    for enemy2 in enemies2:
        enemy2.update(frame_time)
    for enemy3 in enemies3:
        enemy3.update(frame_time)

    for enemy1 in enemies1:
        if collide(enemy1, p_missile):
            p_missile.stop()
            enemy1.missile_on = False
            enemy1.launch = False
            enemy1.stop()
            score = score + 800
    for enemy2 in enemies2:
        if collide(enemy2, p_missile):
            p_missile.stop()
            enemy2.stop()
            score = score + 500
    for enemy3 in enemies3:
        if collide(enemy3, p_missile):
            p_missile.stop()
            enemy3.stop()
            score = score + 300
    pass




def draw(frame_time):
    clear_canvas()
    map.draw()
    fighter.draw()
    p_missile.draw()
    draw_score.draw()
    score2.draw()
    fighter_life.draw()
    for enemy1 in enemies1:
        enemy1.draw()
        enemy1.draw_bb()
    for enemy2 in enemies2:
        enemy2.draw()
        enemy2.draw_bb()
    for enemy3 in enemies3:
        enemy3.draw()
        enemy3.draw_bb()
    p_missile.draw_bb()
    fighter.draw_bb()



    pass

    update_canvas()






