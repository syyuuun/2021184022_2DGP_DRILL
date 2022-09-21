from pico2d import*
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


flag = 0
move_x = 400
move_y = 90
direction = 0
degree = 0
while(True):
    if(flag == 0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(move_x,move_y)
    
        if(direction == 0):
            if(move_x < 800):
                move_x = move_x +2
                move_y = move_y
            else:
                direction = 1
        elif (direction == 1):
            if(move_y < 600):
                move_y = move_y + 2
                move_x = move_x
            else:
                direction = 2            
        elif (direction ==2):
            if(move_x > 0):
                move_x = move_x - 2
                move_y = move_y
            else:
                direction = 3
        elif (direction ==3):
            if(move_y >= 600 & move_x <= 0):
                move_y = move_y - 2
                move_x = move_x
                if(move_y ==90):
                    move_x = 400
                    move_y = 90
                    flag =1
            else:
                direction = 0
    elif(flag ==1):
        pos_x = 400
        pos_y = 90
        clear_canvas_now()
        grass.draw_now(400,30)
        pos_x = math.cos(degree / 360 * 2 * math.pi) * 200 + 400
        pos_y = math.sin(degree / 360 * 2 * math.pi) * 200 + 300
        character.draw_now(pos_x,pos_y)
        degree = degree + 1
        if(degree > 360):
            flag = 0
    delay(0.01)
