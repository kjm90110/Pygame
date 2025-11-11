import pygame
from cactus import Cactus
from scorpion import Scorpion

class Player:
    def __init__(self):
        self.hp = 100 # 체력
        self.hunt = 0 # 전갈 사냥 횟수
        self.score = 0
        self.isJumping = False
        # self.jumpCount = 0
        # 캐릭터 기본 위치
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
        self.velocity = -50
            

    def jump_update(self):
        self.y += self.velocity
        self.velocity += 10
        if self.y >= 400:
            self.y = 400
            # self.jumpCount += 1
            self.isJumping = False


    def hunting(self, scorpion, player_foot, scorpion_back):
        if player_foot.colliderect(scorpion_back):
            self.velocity = -40
            self.isJumping = True
            self.jump_update() 
            self.score+=1
            scorpion.death()

    def hurt(self, enemy):
        if enemy == 'scorpion':
            self.hp -= 40
            return self.hp
        elif enemy == 'cactus':
            self.hp -= 20
            return self.hp
    

    def death_action(self, screen, font):

        # 루프 멈추고 대기
        death = True
        while death:
            # 1️⃣ 반투명 검정 배경 생성
            overlay = pygame.Surface((800, 600))  # 화면 크기와 같게
            overlay.set_alpha(180)  # 0=투명, 255=불투명
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))
            # 2️⃣ "YOU'RE DEAD" 빨간 글씨 표시
            text = font.render("YOU'RE DEAD", True, (255, 0, 0))
            text_rect = text.get_rect(center=(400, 300))
            screen.blit(text, text_rect) 
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER:   # R 누르면 재시작
                        death = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()      

