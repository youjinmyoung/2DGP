from pico2d import *

import game_framework
import title_state
import pause_state
import game_over_state


from map import Map
from fighter import Fighter
from green_enemy import GreenEnemy
#from red_enemy import RedEnemy
#from blue_enemy import BlueEnemy
from missile import FighterMissile, EnemyMissile
from scorenumber import ScoreNumber
from score import Score
from fighterlife import FighterLife

name = "MainState"

map = None
fighter = None
fighter_missile = None
enemy_missile = None
EnemyMissiles = None
green_enemy = None
red_enemy = None
blue_enemy = None
green_enemies = None
red_enemies = None
blue_enemies = None
score_number = 0
score = None
score_data = None
draw_score = None
fighter_life1 = None
fighter_life2 = None
life = 2

green_enemy_data_file = open('green_enemy.txt', 'r')
green_enemy_data = json.load(green_enemy_data_file)
green_enemy_data_file.close()

#red_enemy_data_file = open('red_enemy.txt', 'r')
#red_enemy_data = json.load(red_enemy_data_file)
#red_enemy_data_file.close()

#blue_enemy_data_file = open('blue_enemy.txt', 'r')
#blue_enemy_data = json.load(blue_enemy_data_file)
#blue_enemy_data_file.close()


def create_green_enemy():
    green_enemies = []
    for name in green_enemy_data:
        green_enemy = GreenEnemy()
        green_enemy.name = name
        green_enemy.x = green_enemy_data[name]['x']
        green_enemy.y = green_enemy_data[name]['y']
        green_enemies.append(green_enemy)
    return green_enemies

#def create_red_enemy():
#    red_enemies = []
#    for name in red_enemy_data:
#        red_enemy = RedEnemy()
#        red_enemy.name = name
#        red_enemy.x = red_enemy_data[name]['x']
#        red_enemy.y = red_enemy_data[name]['y']
#        red_enemies.append(red_enemy)
#    return red_enemies

#def create_blue_enemy():
#    blue_enemies = []
#    for name in blue_enemy_data:
#        blue_enemy = BlueEnemy()
#        blue_enemy.name = name
#        blue_enemy.x = blue_enemy_data[name]['x']
#        blue_enemy.y = blue_enemy_data[name]['y']
#        blue_enemies.append(blue_enemy)
#    return blue_enemies

def create_world():
    global map, fighter, fighter_missile, green_enemies, red_enemies, blue_enemies, enemy_missile
    global draw_score, fighter_life1, fighter_life2, score, EnemyMissiles
    map = Map(800,600)

    draw_score = ScoreNumber()
    score = Score()
    fighter = Fighter()
#    green_enemy = GreenEnemy()
    green_enemies = create_green_enemy()
#    red_enemies = create_red_enemy()
#    blue_enemies = create_blue_enemy()
    fighter_missile = FighterMissile()
    #enemy_missile = EnemyMissile()
    EnemyMissiles = [EnemyMissile() for i in range(3)]
    fighter_life1 = FighterLife(30, 30)
    fighter_life2 = FighterLife(80, 30)
    pass


def destroy_world():
    global map, fighter, green_enemies, fighter_missile, red_enemies, blue_enemies, enemy_missile
    global draw_score, fighter_life1, fighter_life2, score, EnemyMissiles

    del(map)
    del(fighter)
    del(green_enemies)
    del(red_enemies)
    del(blue_enemies)
    del(fighter_missile)
    del(enemy_missile)
    del(draw_score)
    del(fighter_life1)
    del(fighter_life2)
    del(score)
    del(EnemyMissiles)

def enter():
    #open_canvas()
    #game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    #close_canvas()

def save_score():
    global score_data, score_number

    f = open('resource/data_file.txt','r')
    score_data = json.load(f)
    f.close()

    score_data.append({'score':score_number})

    f = open('resource/data_file.txt', 'w')
    json.dump(score_data, f)
    f.close()

def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global fighter_missile
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
            fighter_missile.handle_event(event)






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
    global score_number, draw_score, life
    fighter.update(frame_time)
    map.update(frame_time)
    fighter_missile.update(frame_time, fighter.x, fighter.y)
#    enemy_missile.update(frame_time, green_enemies.x, green_enemies.y)
    draw_score.update(frame_time, score_number)
    #green_enemies.update(frame_time)
    for enemy_missile in EnemyMissiles:
        enemy_missile.update(frame_time)


    for green_enemy in green_enemies:
        green_enemy.update(frame_time)
    #for red_enemy in red_enemies:
     #   red_enemy.update(frame_time)
    #for blue_enemy in blue_enemies:
     #   blue_enemy.update(frame_time)

    for green_enemy in green_enemies:
        if collide(green_enemy, fighter_missile):
            fighter_missile.stop()
            green_enemy.die()
            score_number = score_number + 800
    #for red_enemy in red_enemies:
     #   if collide(red_enemy, p_missile):
      #      p_missile.stop()
       #     red_enemy.die()
        #    score = score + 500
    #for blue_enemy in blue_enemies:
     #   if collide(blue_enemy, p_missile):
      #      p_missile.stop()
       #     blue_enemy.die()
        #    score = score + 300
    for enemy_missile in EnemyMissiles:
        if collide(fighter, enemy_missile):
            enemy_missile.stop()
            fighter.die()
            life -= 1
    if life < 0:
        game_framework.push_state(game_over_state)

    pass




def draw(frame_time):
    clear_canvas()
    map.draw()
    fighter.draw()
    fighter_missile.draw()
    #enemy_missile.draw()
    for enemy_missile in EnemyMissiles:
        enemy_missile.draw()
        enemy_missile.draw_bb()
    draw_score.draw()
    score.draw()
    fighter_life1.draw()
    fighter_life2.draw()
    if life == 1:
        fighter_life2.x = -50
    if life == 0:
        fighter_life1.x = -50
    for green_enemy in green_enemies:
        green_enemy.draw()
        green_enemy.draw_bb()
    #for red_enemy in red_enemies:
    #    red_enemy.draw()
    #    red_enemy.draw_bb()
    #for blue_enemy in blue_enemies:
    #    blue_enemy.draw()
    #    blue_enemy.draw_bb()
    fighter_missile.draw_bb()
    #enemy_missile.draw_bb()
    fighter.draw_bb()



    pass

    update_canvas()






