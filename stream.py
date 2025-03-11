import random

import pygame

from text import Text

#  INITIALIZERS
pygame.font.init()

#  CONSTANTS
DISTANCE_Y_BETWEEN_LETTERS = 11
DISTANCE_X_BETWEEN_LETTERS = 10
PINK = (255, 192, 203)
#  TEXTS AND FONTS
love_font = pygame.font.SysFont('Roboto', 20)
LOVE_LETTERS = (love_font.render('L', False, PINK),
                love_font.render('O', False, PINK),
                love_font.render('V', False, PINK),
                love_font.render('E', False, PINK),
                love_font.render('I', False, PINK),
                love_font.render('Y', False, PINK),
             )

class Stream:
    letters: list = []
    max_priorities: int
    x: int
    def __init__(self, x):
        self.letters = []
        self.x = x

    def generate_stream(self):
        priority_variant = random.randint(0, 30)
        #  Column creation
        end = random.randint(20, 60)
        self.max_priorities = end + priority_variant
        for y in range(end):
            letter = random.choice(LOVE_LETTERS)
            self.letters.append(Text(letter, self.x * DISTANCE_X_BETWEEN_LETTERS, y * DISTANCE_Y_BETWEEN_LETTERS, y + priority_variant))

    def soft_exit(self, fade_speed: int):
        for letter in self.letters:
            letter.fade_out(fade_speed)

    def get_x(self) -> int:
        return self.x
