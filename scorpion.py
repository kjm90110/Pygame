import random
import pygame

pygame.init()

class Scorpion:
    def __init__(self):
        self.x = 1500
        self.y = 400
        self.isDeath = False

    scorpion_speed = random.randint(16, 25)
    def move(self):
        if not self.isDeath:
            self.x -= Scorpion.scorpion_speed
            if self.x <= 0:
                self.x = 1500
        else:
            self.death()

    def death(self):
        # 죽는 액션 처리
        self.y += 40
        self.isDeath = True
        