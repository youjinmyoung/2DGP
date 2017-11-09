import game_framework
import title_state
from pico2d import *

import main_state
name = 'PauseState'
image = None
count = 0


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)


def update():
    global count
    count = (count +1) % 200
    pass


def draw():
    clear_canvas()
    main_state.draw_state()
    if count < 100:
        image.draw(400,500)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            # p key go to main_state
            game_framework.pop_state()
    pass


def pause(): pass


def resume(): pass