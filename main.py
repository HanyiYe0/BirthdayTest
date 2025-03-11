import random

import pygame
from stream import Stream
from ball import Ball
#  CONSTANTS
COLUMNS = 108
FADE_SPEED = 35
FADE_OUT_SPEED = 40
FLY_OUT_AMOUNT = 0
#  Initializers
pygame.init()
screen = pygame.display.set_mode((1080, 720))
running = True
clock = pygame.time.Clock()


balls: list[Ball] = []
streams: list[Stream] = []
max_priorities: list[int] = []

#
one_coords = (

    (500, 202), (510, 202), (520, 202), (530, 202), (540, 202), (550, 202),
    (510, 191), (520, 191), (530, 191), (540, 191), (550, 191),
    (520, 180), (530, 180), (540, 180), (550, 180),
    #(530, 169), (540, 169), (550, 169),
    #(540, 158), (550, 158),

    (490, 213), (500, 213), (510, 213),
    (470, 224), (480, 224), (490, 224), (500, 224), (510, 224),
    (460, 235), (470, 235), (480, 235), (490, 235), (500, 235),
    (440, 246), (450, 246), (460, 246), (470, 246), (480, 246), (490, 246),
    (440, 257), (450, 257), (460, 257), (470, 257), (480, 257),
    (440, 268), (450, 268), (460, 268),
    (440, 279), (450, 279), 

    # Vertical stroke (from top down)
    (520, 213), (530, 213), (540, 213), (550, 213),
    (520, 224), (530, 224), (540, 224), (550, 224),
    (520, 235), (530, 235), (540, 235), (550, 235),
    (520, 246), (530, 246), (540, 246), (550, 246),
    (520, 257), (530, 257), (540, 257), (550, 257),
    (520, 268), (530, 268), (540, 268), (550, 268),
    (520, 279), (530, 279), (540, 279), (550, 279),
    (520, 290), (530, 290), (540, 290), (550, 290),
    (520, 301), (530, 301), (540, 301), (550, 301),
    (520, 312), (530, 312), (540, 312), (550, 312),
    (520, 323), (530, 323), (540, 323), (550, 323),
    (520, 334), (530, 334), (540, 334), (550, 334),
    (520, 345), (530, 345), (540, 345), (550, 345),
    (520, 356), (530, 356), (540, 356), (550, 356),
    (520, 367), (530, 367), (540, 367), (550, 367),
    (520, 378), (530, 378), (540, 378), (550, 378),
    (520, 389), (530, 389), (540, 389), (550, 389),

    # Base of the 1 (four horizontal rows)
    # Top row of the base
    (460, 400), (470, 400), (480, 400), (490, 400), (500, 400),
    (510, 400), (520, 400), (530, 400), (540, 400), (550, 400),
    (560, 400), (570, 400), (580, 400), (590, 400), (600, 400),
    (610, 400),

    # Second row of the base
    (460, 411), (470, 411), (480, 411), (490, 411), (500, 411),
    (510, 411), (520, 411), (530, 411), (540, 411), (550, 411),
    (560, 411), (570, 411), (580, 411), (590, 411), (600, 411),
    (610, 411),

    # Third row of the base
    (460, 422), (470, 422), (480, 422), (490, 422), (500, 422),
    (510, 422), (520, 422), (530, 422), (540, 422), (550, 422),
    (560, 422), (570, 422), (580, 422), (590, 422), (600, 422),
    (610, 422),

    # Bottom row of the base
    (460, 433), (470, 433), (480, 433), (490, 433), (500, 433),
    (510, 433), (520, 433), (530, 433), (540, 433), (550, 433),
    (560, 433), (570, 433), (580, 433), (590, 433), (600, 433),
    (610, 433),
)


fly_to_target = False
temp_count = FLY_OUT_AMOUNT
#  COLUMN CREATION SECTION
#  Multiple column creation
for x in range(COLUMNS):
    s = Stream(x)
    streams.append(s)
    s.generate_stream()
    max_priorities.append(s.max_priorities)

#  BALLS CREATION SECTION
for x, y in one_coords:
    balls.append(Ball(x, y))

#  MAIN PROGRAM SECTION
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #  Background
    screen.fill("black")

    #
    #  Streams
    #
    for i in range(len(streams)):
        #  Checker for finished full stream animation
        if max_priorities[i] <= 0:
            #  Fade out
            for letter in streams[i].letters:
                letter.fade_in = False
                letter.fade_out(FADE_OUT_SPEED)
                letter.text.set_alpha(letter.alpha)
                screen.blit(letter.text, (letter.x, letter.y))

            #  All faded out
            if all([letter.faded_out for letter in streams[i].letters]):
                #  Generate new stream and remove old
                new_s = Stream(streams[i].x)
                streams[i] = new_s
                new_s.generate_stream()
                max_priorities[i] = new_s.max_priorities

        max_priorities[i] -= 1

        #  Stream animation
        for letter in streams[i].letters:
            #  Fade in, fade out animation
            letter.fade(FADE_SPEED)
            letter.text.set_alpha(letter.alpha)
            screen.blit(letter.text, (letter.x, letter.y))

    #
    #  Numbers
    #
    for ball in balls:
        #  Fly out
        if temp_count >= 0 and not fly_to_target:
            ball.fly_out()
            temp_count -= 1
        else:
            fly_to_target = True

        #  Fly to target
        if fly_to_target:
            if temp_count <= FLY_OUT_AMOUNT + 2000:
                temp_count += 1
            # else:
            #     fly_to_target = False
            ball.move_towards_target()

        #  Update the ball
        ball.draw(screen)

    pygame.display.flip()
    clock.tick(15)
pygame.quit()
