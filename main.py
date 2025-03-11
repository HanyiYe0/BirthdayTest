import random
import pygame
import threading
from text import Text

#  CONSTANTS
COLUMNS = 108
DISTANCE_Y_BETWEEN_LETTERS = 11
DISTANCE_X_BETWEEN_LETTERS = 10
FADE_SPEED = 40
PINK = (255, 192, 203)

#  Initializers
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1080, 720))
running = True
clock = pygame.time.Clock()

#  TEXTS AND FONTS
love_font = pygame.font.SysFont('Roboto', 20)
LOVE_LETTERS = (love_font.render('L', False, PINK),
                love_font.render('O', False, PINK),
                love_font.render('V', False, PINK),
                love_font.render('E', False, PINK),
                love_font.render('I', False, PINK),
                love_font.render('Y', False, PINK),
             )

#  COLUMN CREATION SECTION
letters = []
max_priorities = []
#  Multiple column creation
for x in range(COLUMNS):
    priority_variant = random.randint(0, 20)
    #  Column creation
    end = random.randint(10, 50)
    max_priorities.append(end)
    for y in range(end):
        letter = random.choice(LOVE_LETTERS)
        letters.append(Text(letter, x * DISTANCE_X_BETWEEN_LETTERS, y * DISTANCE_Y_BETWEEN_LETTERS, y + priority_variant))

#  MAIN PROGRAM SECTION
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #  Background
    screen.fill("black")

    #  Stream animation
    for letter in letters:
        #  Fade in, fade out animation
        letter.fade(FADE_SPEED)
        letter.text.set_alpha(letter.alpha)
        screen.blit(letter.text, (letter.x, letter.y))
    pygame.display.flip()
    clock.tick(10)
pygame.quit()
