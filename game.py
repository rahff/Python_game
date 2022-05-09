
import pygame
from pygame import sprite
from pygame.sprite import Group, Sprite, collide_rect
from pygame.surface import Surface
from player import Player
from monster import Monster
import time


class Game(pygame.sprite.Sprite):

    def __init__(self, screen: Surface, background) -> None:
        self.running = True
        self.screen = screen
        self.background = background
        self.player = Player()
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        self.heart_beat = 1
        self.level = 1

    def main(self) -> None:
        while self.running:
            self.draw_sprite()
            self.dispatch_event()
            self.listen_event()
            self.check_monster_collision(self.all_monster)
            self.heart_beat += 1
            pygame.display.flip()

    def dispatch_event(self) -> None:
        if self.pressed.get(pygame.K_RIGHT):
            self.player.move_right(self.screen.get_width())
        elif self.pressed.get(pygame.K_LEFT):
            self.player.move_left()
        elif self.pressed.get(pygame.K_SPACE):
            self.player.put_the_hand_up()
        
    def listen_event(self) -> None:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True
                if event.key == pygame.K_SPACE:
                    self.player.launch_projectil()
            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False
                if event.key == pygame.K_SPACE:
                    self.player.put_the_hand_down()

    def draw_sprite(self) -> None:
        self.screen.blit(self.background, (0,-200))
        self.screen.blit(self.player.image, self.player.rect)
        
        for projectil in self.player.all_projectils:
            projectil.move()

        for monster in self.all_monster:
            if self.heart_beat % 2 == 0:
                self.animate_monster(monster)
                self.check_monster(monster)

        self.player.all_projectils.draw(self.screen)
        self.all_monster.draw(self.screen)

    def spawn_monster(self) -> None:
        monster = Monster()
        self.all_monster.add(monster)

    def animate_monster(self, monster: Monster) -> None:
        monster.move()
        if self.heart_beat % 10 == 0:
            self.heart_beat = monster.walk(self.heart_beat)
        
    def check_monster(self, monster: Monster) -> None:
        if monster.rect.x < 0:
            self.destroy_monster(monster)

    def check_monster_collision(self, monsters: Group):
        for monster in monsters:
            if pygame.sprite.collide_rect(monster, self.player):
                self.onCollisionPlayer()
                monster.blocked = True
                if self.heart_beat % 10 == 0:
                    monster.mummy_attack()
                
            elif self.player.all_projectils.sprites().__len__() > 0 :
                if pygame.sprite.collide_rect(self.player.all_projectils.sprites()[0], monster):
                    current_sprite = self.player.all_projectils.sprites()[0]
                    monster.blocked = True
                    monster.health -= 34
                    if monster.health < 0:
                        self.destroy_monster(monster)
                    time.sleep(0.1)
                    self.player.all_projectils.remove(current_sprite)

            else:
                self.player.blocked = False
                monster.blocked = False

    def onCollisionPlayer(self):
        self.player.blocked = True
        self.player.healf -= 20
        if self.player.rect.x < 0:
            self.player.rect.x -=20
        if(self.player.healf <= 0):
            self.player.remove()

    def destroy_monster(self, monster) -> None:
        self.all_monster.remove(monster)
        self.spawn_monster()