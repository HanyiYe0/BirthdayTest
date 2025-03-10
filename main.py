import random
import asyncio
import pygame

from text import Text

#  CONSTANTS
DISTANCE_BETWEEN_LETTERS = 11
FADE_SPEED = 30
PINK = (255, 192, 203)

def fade_out(text: pygame.font, x: int, y: int) -> None:
    for i in range(255, -1, -1):
        text.set_alpha(i)
        screen.blit(text, (x, y * DISTANCE_BETWEEN_LETTERS))
        pygame.display.flip()
        print(i)
        pygame.time.delay(FADE_SPEED)

def fade_in(text: pygame.font, x: int, y: int) -> None:
    for i in range(256):
        text.set_alpha(i)
        screen.blit(text, (x, y * DISTANCE_BETWEEN_LETTERS))
        pygame.display.flip()
        print(i)
        pygame.time.delay(FADE_SPEED)



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

letters = []
#  Background text flowing
for y in range(1): #random.randint(20, 50)):
    letter = random.choice(LOVE_LETTERS)
    letters.append(Text(letter, 0, y * DISTANCE_BETWEEN_LETTERS))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Background
    screen.fill("black")

    for letter in letters:
        letter.fade(FADE_SPEED)
        letter.text.set_alpha(letter.alpha)
        screen.blit(letter.text, (letter.x, letter.y))

    pygame.display.flip()

    clock.tick(10)
pygame.quit()
