import game_framework
from pico2d import *

import main_state
name = 'ClearState'
image = None
sound = None

def enter():
    global image, sound
    image = load_image('resource/clear.png')
    sound = load_music('sounds/clear.mp3')
    sound.set_volume(32)
    sound.play()

def exit():
    global image
    del(image)

def update(frame_time):

    pass

def draw(frame_time):
    clear_canvas()
    main_state.draw(frame_time)
    image.draw(400,300)
    update_canvas()
    delay(0.1)
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