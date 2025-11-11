import pygame
from player import Player
from cactus import Cactus
from scorpion import Scorpion
pygame.init()

def initGame():
    global screen_width, screen_height, screen, clock, font, background_img, cactus_img, character_img, scorpion_img, star_img, desert_draw, cactus_draw, character_draw, scorpion_draw, star_draw

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
    star_img = pygame.image.load('./images/star1.png')

    # load한 이미지들을 두 번째 인자로 준 튜플(가로세로 px)에 맞게 사이즈 조정 해서 
    # 랜더링 준비 상태로 만든다. 
    desert_draw = pygame.transform.scale(background_img, (screen_width, screen_height))
    cactus_draw = pygame.transform.scale(cactus_img, (180, 300))
    character_draw = pygame.transform.scale(character_img, (150, 150))
    scorpion_draw = pygame.transform.scale(scorpion_img, (100, 100))
    star_draw = pygame.transform.scale(star_img, (30, 30))

    gameActivate()


def gameActivate():
    
    player = Player()
    cactus = Cactus()
    scorpion = Scorpion()

    isConflictScorpion = False
    isConflictCactus = False

    running = True 
    while running:

        clock.tick(30)

        score = font.render('score: ' + str(player.score), True, (0, 0, 0))
        hp = font.render('hp: ' + str(player.hp), True, (0,0,0))
        player.game_start(pygame.key.get_pressed())

        # 실제로 게임 화면에 이미지를 그려주는 blit 메서드드
        # 화면에 배경 그리기(이미지, 좌표)
        screen.blit(desert_draw, (0, 0)) 

        for event in pygame.event.get(): # event 감지
            if event.type == pygame.QUIT: # x 누르면 게임 종료됨
                running = False
            elif event.type == pygame.KEYDOWN: # 키를 눌렀는데
                if event.key == pygame.K_SPACE: # 눌러진 키가 스페이스바일 경우우
                    player.jump() # player 객체의 jump 인스턴스 메서드

        # jump 감지되면 프레임마다 update 되도록 하는 jump_update method
        player.jump_update()

        cactus.update()
        scorpion.move()
        
        if scorpion.isDeath: # 만약 기존 전갈이 죽으면
            scorpion = Scorpion() # 새로운 객체로 변경

        screen.blit(cactus_draw, (cactus.x, cactus.y)) # 화면에 선인장 그리기(이미지, 좌표)
        screen.blit(character_draw, (player.x, player.y)) # 화면에 캐릭터 그리기
        screen.blit(scorpion_draw, (scorpion.x, scorpion.y)) # 화면에 전갈 그리기
        
        screen.blit(star_draw, (20, 50)) # 별(점수 표시)
        screen.blit(score, (50, 50))
        screen.blit(hp, (50, 90))

        # 충돌 처리
        character_rect = pygame.Rect(player.x, player.y, 50, 50)
        scorpion_rect = pygame.Rect(scorpion.x, scorpion.y, 50, 50)
        cactus_rect = pygame.Rect(cactus.x, cactus.y, 30, 100)

        
        # a_rect.colliderect(b_rect): a_rect 객체가 b_rect 객체와 
        # 충돌 중인지에 대한 boolean 데이터.
        # 선인장 또는 전갈과 닿을 경우 hp 깎임
        if character_rect.colliderect(scorpion_rect) and not isConflictScorpion:
            hp = player.hurt('scorpion')
            if hp <= 0:
                player.death_action(screen, font)
            isConflictScorpion = True  # 충돌 상태 시작

        elif character_rect.colliderect(cactus_rect) and not isConflictCactus:
            hp = player.hurt('cactus')
            if hp <= 0:
                player.death_action(screen, font)
            isConflictCactus = True 

        elif not character_rect.colliderect(scorpion_rect):
            isConflictScorpion = False  # 충돌 끝나면 다시 False

        elif not character_rect.colliderect(cactus_rect):
            isConflictCactus = False  


        # 전갈의 등을 밟을 경우 전갈이 죽게 하기 위해
        # rect 객체를 이용해서 맞닿는 영역을 만든다.
        # 플레이어의 발 영역 rect
        player_foot = pygame.Rect(character_rect.left, character_rect.bottom, character_rect.width, 10)
        # 전갈의 등 영역 rect
        scorpion_back = pygame.Rect(scorpion_rect.left, scorpion_rect.top, 100, 10)    

        player.hunting(scorpion, player_foot, scorpion_back)

        pygame.display.update() 

if __name__ == '__main__':
    initGame()