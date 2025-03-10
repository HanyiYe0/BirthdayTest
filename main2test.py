import random
import pygame

# CONSTANTS
DISTANCE_BETWEEN_LETTERS = 11
FADE_SPEED = 5  # Lower value = faster fade
PINK = (255, 192, 203)

# Initializers
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()

# TEXTS AND FONTS
love_font = pygame.font.SysFont('Roboto', 20)
LOVE_LETTERS = (
    love_font.render('L', False, PINK),
    love_font.render('O', False, PINK),
    love_font.render('V', False, PINK),
    love_font.render('E', False, PINK),
    love_font.render('I', False, PINK),
    love_font.render('Y', False, PINK),
)

# Animation state
class FadingText:
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y
        self.alpha = 0
        self.fade_in = True

    def update(self):
        if self.fade_in:
            self.alpha += FADE_SPEED
            if self.alpha >= 255:
                self.alpha = 255
                self.fade_in = False
        else:
            self.alpha -= FADE_SPEED
            if self.alpha <= 0:
                self.alpha = 0
                self.fade_in = True

    def draw(self):
        self.text.set_alpha(self.alpha)
        screen.blit(self.text, (self.x, self.y))

# Create a list of fading text objects
fading_texts = []
for y in range(10):  # Create 10 rows of text
    letter = random.choice(LOVE_LETTERS)
    fading_texts.append(FadingText(letter, 0, y * DISTANCE_BETWEEN_LETTERS))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill("black")

    # Update and draw fading texts
    for text in fading_texts:
        text.update()
        text.draw()

    # Update the display
    pygame.display.flip()
    clock.tick(60)  # Cap the frame rate to 60 FPS

pygame.quit()
