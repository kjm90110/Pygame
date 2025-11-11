import pygame
from player import Player
from cactus import Cactus
from scorpion import Scorpion
pygame.init()

# screen setting
screen_width, screen_height = 1200, 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Desert Run")

clock = pygame.time.Clock()

font = pygame.font.SysFont('bahnschrift', 40)

# image load
background_img = pygame.image.load('./images/desert.png')
cactus_img = pygame.image.load('./images/cactus.png')
character_img = pygame.image.load('./images/charactor.png')
scorpion_img = pygame.image.load('./images/scorpion.png') 

desert_draw = pygame.transform.scale(background_img, (screen_width, screen_height))
cactus_draw = pygame.transform.scale(cactus_img, (180, 200))
character_draw = pygame.transform.scale(character_img, (150, 150))
scorpion_draw = pygame.transform.scale(scorpion_img, (50, 50))


player = Player()
cactus = Cactus()
scorpion = Scorpion()

running = True 
while running:

    clock.tick(30)

    score = font.render(str(player.score), True, (0, 0, 0))
    hp = font.render(str(player.hp), True, (0,0,0))
    player.game_start(pygame.key.get_pressed())
            
    screen.blit(desert_draw, (0, 0)) # 화면에 배경 그리기(이미지, 좌표)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    # jump 감지되면 프레임마다 update 되도록
    player.jump_update()
    cactus.update() 
    scorpion.move()

    screen.blit(cactus_draw, (cactus.x, cactus.y)) # 화면에 선인장 그리기(이미지, 좌표)
    screen.blit(character_draw, (player.x, player.y)) # 화면에 캐릭터 그리기
    screen.blit(score, (50, 50))
    screen.blit(hp, (50, 70))

    # 충돌 처리
    character_rect = pygame.Rect(player.x, player.y, 50, 50)
    scorpion_rect = scorpion_draw.get_rect()
    cactus_rect = pygame.Rect(cactus.x, cactus.y, 30, 100)

    if character_rect.colliderect(scorpion_rect):
        hp = player.hurt('scorpion')
        if hp == 0:
            player.death_action()
    elif character_rect.colliderect(cactus_rect):
        hp = player.hurt('cactus')
        if hp == 0:
            player.death_action()
    
    pygame.display.update() 
