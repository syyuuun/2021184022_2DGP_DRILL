from pico2d import *
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas()
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
player_x = 400
player_y = 90
frame_bottom = 0
frame =0
dir_x = 0
dir_y = 0
def handle_events():
    global running
    global dir_x
    global dir_y
    global frame_bottom
    global player_y
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                dir_x -=1
                frame_bottom = 0
            elif event.key == SDLK_RIGHT:
                dir_x +=1
                frame_bottom = 100
            elif event.key == SDLK_UP:
                dir_y +=1
            elif event.key == SDLK_DOWN:
                dir_y -=1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                dir_x +=1
                frame_bottom = 200
            elif event.key == SDLK_RIGHT:
                dir_x -=1
                frame_bottom = 300
            elif event.key == SDLK_UP:
                dir_y -=1
            elif event.key == SDLK_DOWN:
                dir_y +=1
while running:
    handle_events()
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame*100,frame_bottom,100,100,player_x,player_y)
    player_x += dir_x*5
    player_y += dir_y*5
    frame = (frame + 1) % 8
    delay(0.05)
    update_canvas()
close_canvas()