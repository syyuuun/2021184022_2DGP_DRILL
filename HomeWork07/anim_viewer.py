from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('space.png')

x = 0
frame = 0
yPos = 0
while True:
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame * 100,yPos, 100, 100, 400,90)
    update_canvas()
    frame = (frame+1) % 6
    if frame == 0:
        yPos = yPos + 100
    if yPos >= 500:
        yPos = 0
    x = x+5
    delay(0.05)
    get_events()

close_canvas()