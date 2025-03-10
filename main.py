import random

import pygame
from collections.abc import Collection

#  Initializers
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1080, 720))
running = True
clock = pygame.time.Clock()

#  TEXTS AND FONTS
love_font = pygame.font.SysFont('Roboto', 20)
LOVE_LETTERS = (love_font.render('L', False, (255, 192, 203)),
                love_font.render('O', False, (255, 192, 203)),
                love_font.render('V', False, (255, 192, 203)),
                love_font.render('E', False, (255, 192, 203)),
love_font.render('I', False, (255, 192, 203)),
love_font.render('Y', False, (255, 192, 203)),
             )

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Background
    screen.fill("black")

    #  Background text flowing
    for y in range(random.randint(20, random.randint(20, 60))):
        letter = random.choice(LOVE_LETTERS)
        screen.blit(letter, (0, y * 11))

    pygame.display.flip()
    clock.tick(1)
pygame.quit()
