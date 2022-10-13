import pico2d
import random
from pico2d import *
import game_framework
import logo_state
import title_state
import item_state

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)
class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0,7)
        self.dir = 1
        self.image = load_image('animation_sheet.png')
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')
        self.item = None

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        if self.x > 800:
            self.dir = -1
            self.x = 800
        elif self.x < 0:
            self.dir = 1
            self.x = 0

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_b:
                game_framework.push_state(item_state)

# 게임 초기화: 객체들을 생성

grass = None
team = None
nBoys = 1
def enter():
    global team, grass, nBoys
    team = [Boy()]
    grass = Grass()

# 게임 월드에 객체를 업데이트 - 게임 로직+
def update():
    global team
    for boy in team:
        boy.update()

def draw_world():
    grass.draw()
    for boy in team:
        boy.draw()

 # 게임 월드 렌더링
def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass


def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()

if __name__ == '__main__':  # 만약 단독 실행 상태이면
    test_self()


# 게임 종료 - 객체를 소멸
def exit():
    global boy, grass
    del boy
    del grass

# open_canvas()
# enter()
#
# # game main loop code
# while running:
#     handle_events()
#     update()
#     draw()
#     delay(0.05)
# exit()
# # finalization code
# close_canvas()


