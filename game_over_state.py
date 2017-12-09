import game_framework
import title_state
from pico2d import *

import main_state
name = 'GameOverState'
image = None
count = 0
def enter():
    global image
    image = load_image('resource/gameover.png')

def exit():
    global image
    del(image)

def update(frame_time):
    global count
    count = (count + 1) % 200
    pass

def draw(frame_time):
    clear_canvas()
    main_state.draw(frame_time)
    if count < 50:
        image.draw(400,300)
    update_canvas()
    pass

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
    pass

def pause(): pass

def resume(): pass