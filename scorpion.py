import random
import pygame

pygame.init()

# 전갈 Class
class Scorpion:
    def __init__(self):
        # 위치, 죽음 여부
        self.x = 1500
        self.y = 400
        self.isDeath = False

    # 달려오는 속도는 랜덤
    scorpion_speed = random.randint(15, 25)

    # 플레이어에게 다가오는 메서드
    def move(self):
        if not self.isDeath:
            self.x -= Scorpion.scorpion_speed
            if self.x <= 0:
                self.x = 1500
        else:
            self.death()

    def death(self):
        # 죽는 액션 처리
        self.y += 50 # 아래로 50px 꺼짐
        self.isDeath = True
        