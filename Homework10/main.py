import pico2d
import play_state
import logo_state
import title_state
pico2d.open_canvas()
states = [logo_state, play_state] # 모듈을 변수로 취급

# game main loop code
for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
        pico2d.delay(0.05)
    state.exit()

# finalization code
pico2d.close_canvas()
