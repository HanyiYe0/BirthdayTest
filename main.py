import pygame
from stream import Stream

#  CONSTANTS
COLUMNS = 108
FADE_SPEED = 40

#  Initializers
pygame.init()
screen = pygame.display.set_mode((1080, 720))
running = True
clock = pygame.time.Clock()


streams = []
max_priorities = []

#  COLUMN CREATION SECTION
#  Multiple column creation
for x in range(COLUMNS):
    s = Stream(x)
    streams.append(s)
    s.generate_stream()
    max_priorities.append(s.max_priorities)


#  MAIN PROGRAM SECTION
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #  Background
    screen.fill("black")

    for i in range(len(streams)):
        #  Checker for finished full stream animation
        if max_priorities[i] <= 0:
            #  Fade out
            for letter in streams[i].letters:
                letter.fade_in = False
                letter.fade_out(FADE_SPEED)
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

    pygame.display.flip()
    clock.tick(10)
pygame.quit()
