import pygame
import sys
import Player
import random

pygame.init()

# screen setting
screen_width, screen_height = 1200, 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Desert Run")

clock = pygame.time.Clock()

# image load
background = pygame.image.load('./images/desert.png')
cactus = pygame.image.load('./images/cactus.png')
character = pygame.image.load('./images/charactor.png')

desert = pygame.transform.scale(background, (screen_width, screen_height))
cactus = pygame.transform.scale(cactus, (180, 200))
character = pygame.transform.scale(character, (150, 150))

# 캐릭터 처음 기본 위치
character_x_pos = 200
character_y_pos = 400

# 선인장 기본 위치
cactus_x = 1500
cactus_y = 400

catus_speed = random.randint(5, 10)

# 점프 속도와 상태
velocity = 0
is_jumping = False

running = True 
while running:

    cactus_x -= catus_speed
    if cactus_x < 0:
        cactus_x = 1500

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT: # 창을 닫는 이벤트가 발생할 경우
            running = False # 게임 종료
        
        elif event.type == pygame.K_DOWN:
            if event.key == pygame.K_RIGHT:
                character_x_pos += 30 
            elif event.key == pygame.K_LEFT:
                character_x_pos -= 30
            elif event.key == pygame.K_SPACE:
                velocity = -10
                is_jumping = True
            

    if is_jumping:
        velocity += 28
        character_y_pos = velocity

        if character_y_pos > 400:
            character_y_pos = 400
            is_jumping = False
            velocity = 0
                
                
    screen.blit(desert, (0, 0)) # 화면에 배경 그리기(이미지, 좌표)
    screen.blit(cactus, (cactus_x, cactus_y)) # 화면에 선인장 그리기(이미지, 좌표)
    screen.blit(character, (character_x_pos, character_y_pos)) # 화면에 캐릭터 그리기

    pygame.display.update() 
    clock.tick(30)
