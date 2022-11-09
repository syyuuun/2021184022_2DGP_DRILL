from pico2d import *
from random import randint
import game_framework
import game_world

PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KPH = 20.0 # km/h 마라토너의 평속
RUN_SPEED_MPM = RUN_SPEED_KPH * 1000.0 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Bird:
    def __init__(self):
        self.x,self.y = randint(0,1600),300
        self.image = load_image("bird_animation.png")
        self.frame = 0
        self.face_dir = 1

    def update(self):
        if 1600 < self.x:
            self.face_dir = -1
        if 0 > self.x:
            self.face_dir = 1

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        self.x += self.face_dir * RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        if -1 == self.face_dir:
            self.image.clip_composite_draw(0,0, 165, 190, 0, 'h',int(self.frame) * self.x, self.y,190,190)
        else:
            self.image.clip_composite_draw(0,0, 165, 190, 180, 'h',int(self.frame) * self.x, self.y,190,190)
        pass

