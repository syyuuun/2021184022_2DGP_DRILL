from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024



def handle_events():
   global running
   global x,y
   global events
   global dir
   events = get_events()
   for event in events:
       if event.type == SDL_QUIT:
           running = False
       elif event.type == SDL_KEYDOWN:
           if event.key == SDLK_ESCAPE:
               running = False
           if event.key == SDLK_RIGHT:
               dir += 1
               x += 10
           elif event.key == SDLK_LEFT:
               dir -= 1
               x -= 10
           elif event.key == SDLK_UP:
               y += 10
           elif event.key == SDLK_DOWN:
               y -= 10

open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image("TUK_GROUND.png")
character = load_image("animation_sheet.png")

running = True
x,y = TUK_WIDTH // 2, TUK_HEIGHT //2
frame = 0
dir = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT //2)
    if dir == -1:
        character.clip_draw(frame * 800, 400, 100, 100, x, y)
    elif dir == 1:
        character.clip_draw(frame * 800, 200, 100, 100, x, y)
    elif dir == 0:
        character.clip_draw(frame * 800, 100, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dir * 2
    delay(0.01)

close_canvas()