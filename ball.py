import math
import random

import pygame


class Ball:
    """
    Small balls that will be animated.

    === Attributes ===
    x: x coordinate of the ball
    y: y coordinate of the ball
    target_x: the target x coordinate of the ball
    target_y: the target y coordinate of the ball
    radius: radius of the ball
    speed: speed that the ball moves in
    flyout_angle: the angle that the ball will
                  fly out towards when the function fly out is called
    """
    x: int = 540
    y: int = 350
    target_x: int
    target_y: int
    radius: int = 5
    speed: int = 10
    flyout_angle: int


    def __init__(self, target_x: int, target_y: int):
        self.target_x = target_x
        self.target_y = target_y
        self.flyout_angle = random.randint(0, 360)

    def move_towards_target(self):
        if self.speed < self._calculate_distance():
            angle = math.atan2(self.target_y - self.y, self.target_x - self.x)
            self.x += self.speed * math.cos(angle)
            self.y += self.speed * math.sin(angle)
        else:
            self.x = self.target_x
            self.y = self.target_y

    def _calculate_distance(self) -> float:
        return math.sqrt((self.x - self.target_x)**2 + (self.y - self.target_y)**2)

    def fly_out(self):
        self.x += self.speed * math.cos(self.flyout_angle)
        self.y += self.speed * math.sin(self.flyout_angle)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.x), int(self.y)), self.radius)
