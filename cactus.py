import random

class Cactus:
    # 선인장 기본 위치
    def __init__(self):
        self.x = 1500
        self.y = 320

    # 속도는 랜덤(5~10 사이)
    catus_speed = random.randint(10, 25)

    def update(self):
        self.x -= Cactus.catus_speed
        if self.x < 0:
            self.x = 1500