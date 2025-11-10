import pygame
import sys

pygame.init()

# image load
background = pygame.image.load('./images/desert.png')
cactus = pygame.image.load('./images/cactus.png')
character = pygame.image.load('./images/charactor.png')


# screen setting
screen_width, screen_height = 1200, 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Desert Run")

character_x_pos = 200
character_y_pos = 200

running = True 
while running:
    desert = pygame.transform.scale(background, (screen_width, screen_height))
    screen.blit(desert, (0, 0)) # 화면에 배경 그리기(이미지, 좌표)
    
    cactus = pygame.transform.scale(cactus, (80, 300))
    screen.blit(cactus, (80, 300)) # 화면에 선인장 그리기(이미지, 좌표)

    character = pygame.transform.scale(character, (150, 150))
    screen.blit(character, (character_x_pos, character_y_pos)) # 화면에 캐릭터 그리기

    pygame.display.update() 

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT: # 창을 닫는 이벤트가 발생할 경우
            running = False # 게임 종료
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                character_x_pos += 30 
            elif event.key == pygame.K_LEFT:
                character_x_pos -= 30
            elif event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                character_y_pos += 30
                

        elif event.type == pygame.K_ESCAPE:
            running = False