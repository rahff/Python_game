import pygame


class Projectil(pygame.sprite.Sprite):

    def __init__(self, player) -> None:
        super().__init__()
        self.velocity = 3.5
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + player.rect.width/1.6
        self.rect.y = player.rect.y + player.rect.width/2.5
        self.player = player
        self.origin_image = self.image
        self.angle = 0


    def rotate(self):
        self.angle += 7
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        if(self.rect.x > 1080):
            self.remove()
            
    def remove(self):
        self.player.all_projectils.remove(self)
