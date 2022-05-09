
from game import Game
import pygame
pygame.init()

pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/bg.jpg')

game = Game(screen, background)

game.main()

