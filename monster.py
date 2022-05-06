import pygame
from pygame import image

class Monster(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1080 - self.rect.width
        self.rect.y = 540
        self.blocked = False
    
    def move(self) -> None:
        if self.blocked == False:
            self.rect.x -= 1
    
    def walk(self, counter: int) -> int:
        if(counter/10 < 25):
            self.image = pygame.image.load(f'assets/mummy/mummy{int(counter/10)}.png')
        if(counter/10 == 25):
            counter = 1
        return counter
    
    def mummy_attack(self) :
        self.image = pygame.image.load('assets/mummy_attack.png')
                


