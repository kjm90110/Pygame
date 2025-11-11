import pygame
from cactus import Cactus
from scorpion import Scorpion

class Player:
    def __init__(self):
        self.hp = 100 # 체력
        self.hunt = 0 # 전갈 사냥 횟수
        self.score = 0
        self.isJumping = False
        # 캐릭터 처음 기본 위치
        self.x = 200
        self.y = 400
        self.velocity = 0

    def game_start(self, keys):

        cactus = Cactus()
        cactus.update()

        if keys[pygame.K_RIGHT]:
            self.x += 30 
        elif keys[pygame.K_LEFT]:
            self.x -= 30

    def jump(self):
        self.isJumping = True 
        self.velocity = -60

    def jump_update(self):
        self.y += self.velocity
        self.velocity += 10
        if self.y >= 400:
            self.y = 400
            self.isJumping = False

    def hunting(self):
        pass    

    def hurt(self, enemy):
        print('공격당함!')
        if enemy == 'scorpion':
            self.hp -= 40
            return 
        elif enemy == 'cactus':
            self.hp -= 20
            return
        return self.hp
    

    def death_action(self):
        pass

