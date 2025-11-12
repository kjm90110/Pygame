import pygame
from cactus import Cactus

class Player:
    def __init__(self):
        self.hp = 100 # 체력
        self.hunt = 0 # 전갈 사냥 횟수
        self.score = 0
        self.isJumping = False
        # 캐릭터 기본 위치
        self.x = 200
        self.y = 400
        # 점프 했을 때 가해지는 가속도
        self.velocity = 0

    def game_start(self, keys, screen, font):

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
            self.hp -= 20
            return self.hp
        elif enemy == 'cactus':
            self.hp -= 10
            return self.hp
        
    
    def clear(self, screen, font):
        
        isClear = False
        if self.score==3:
            isClear = True
            while isClear:
                overlay = pygame.Surface((1200, 600))  # 화면 크기와 같게
                overlay.set_alpha(180)  # 0=투명, 255=불투명
                overlay.fill((204, 204, 74))
                screen.blit(overlay, (0, 0))

                text = font.render("Clear!", True, (255, 255, 255))
                text_rect = text.get_rect(center=(600, 300))
                screen.blit(text, text_rect) 
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
    

    def death_action(self, screen, font):

        # 루프 멈추고 대기
        death = True
        while death:
            # 반투명 검정 배경 생성
            overlay = pygame.Surface((1200, 600))  # 화면 크기와 같게
            overlay.set_alpha(180)  # 0=투명, 255=불투명
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))
            # "YOU'RE DEAD" 빨간 글씨 표시
            text = font.render("YOU'RE DEAD", True, (255, 0, 0))
            text_rect = text.get_rect(center=(600, 300))
            screen.blit(text, text_rect) 
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:   # enter 누르면 재시작
                        death = False
                        return 'restart'

                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()      

