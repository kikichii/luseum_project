import pygame
from pygame.display import update

pygame.init()

dis = pygame.display.set_mode((500, 400))
pygame.display.update()
pygame.display.set_caption('Змейка 2', 'snake.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False