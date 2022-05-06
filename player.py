import pygame
from projectil import Projectil

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.healf = 100
        self.max_healf = 100
        self.attach = 10
        self.velocity = 2
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 530
        self.all_projectils = pygame.sprite.Group()
        self.blocked = False

    def move_right(self, limit: int):
        if self.blocked == False:
            if self.rect.x < limit - self.rect.width:
                self.rect.x += self.velocity
    
    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= self.velocity
        
    def launch_projectil(self):
        self.all_projectils.add(Projectil(self))
