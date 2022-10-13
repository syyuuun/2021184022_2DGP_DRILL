from pico2d import *
import game_framework
import play_state
import title_state
# fill here
image = None
running = True
logo_time = 0.0

def enter():
    # fill here
    global image, logo_time, running
    image = load_image("add_delete_boy.png")
    logo_time = 0.0
    running = True
    pass

def exit():
    # fill here
    global image
    del image
    pass

def update():
    pass

def draw():
    # fill here
    clear_canvas()
    play_state.draw_world()
    image.draw(400,300)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_PLUS:
                    play_state.team += [play_state.Boy()]
                    game_framework.pop_state()
                case pico2d.SDLK_MINUS:
                    if play_state.nBoys > 1:
                        play_state.team -=[play_state.Boy()]
                    game_framework.pop_state()

def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()

if __name__ == '__main__':  # 만약 단독 실행 상태이면
    test_self()

