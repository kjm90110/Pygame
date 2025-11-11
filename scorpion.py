import random

class Scorpion:
    def __init__(self):
        self.x = 1500
        self.y = 400

    scorpion_speed = random.randint(10, 25)
    def move(self):
        self.x -= Scorpion.scorpion_speed
        if self.x == 0:
            self.x = 1500

    def death(self):
        # 죽는 액션 처리
        pass