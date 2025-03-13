import random

from ball import Ball
from coordinate import Coordinate



class Animation:
    """
    balls: a list of balls that will be animated
    done: whether the animation is done running.
    """
    name: str
    balls: list[Ball]
    completed: list

    def __init__(self):
        self.balls = [Ball(0, 0) for _ in range(1000)]
        self.completed = []

    def animate_1(self, screen):
        self.set_up_balls_target(Coordinate.one_coords)

        for ball in self.balls:
            ball.move_towards_target()
            ball.draw(screen)

        if all([ball.in_pos for ball in self.balls]):
            if Coordinate.one not in self.completed:
                self.completed.insert(0, Coordinate.one)

    def animate_2(self, screen):
        self.set_up_balls_target(Coordinate.two_coords)

        for ball in self.balls:
            ball.move_towards_target()
            ball.draw(screen)

        if all([ball.in_pos for ball in self.balls]):
            if Coordinate.two not in self.completed:
                self.completed.insert(0, Coordinate.two)

    def animate_3(self, screen):
        self.set_up_balls_target(Coordinate.three_coords)

        for ball in self.balls:
            ball.move_towards_target()
            ball.draw(screen)

        if all([ball.in_pos for ball in self.balls]):
            if Coordinate.three not in self.completed:
                self.completed.insert(0, Coordinate.three)

    def set_up_balls_target(self, animate_this: list):
        #  setup ball target
        match animate_this:
            case Coordinate.one_coords:
                for i in range(len(Coordinate.one_coords)):
                    self.balls[i].in_pos = False
                    self.balls[i].target_x = Coordinate.ONE_INITIAL[0] + Coordinate.one_coords[i][0] * 10
                    self.balls[i].target_y = Coordinate.ONE_INITIAL[1] + Coordinate.one_coords[i][1] * 11
                self._set_to_centre(Coordinate.one_coords)

            case Coordinate.two_coords:
                for i in range(len(Coordinate.two_coords)):
                    self.balls[i].in_pos = False
                    self.balls[i].target_x = Coordinate.TWO_INITIAL[0] + Coordinate.two_coords[i][0] * 10
                    self.balls[i].target_y = Coordinate.TWO_INITIAL[1] + Coordinate.two_coords[i][1] * 11
                self._set_to_centre(Coordinate.two_coords)

            case Coordinate.three_coords:
                for i in range(len(Coordinate.three_coords)):
                    self.balls[i].in_pos = False
                    self.balls[i].target_x = Coordinate.THREE_INITIAL[0] + Coordinate.three_coords[i][0] * 10
                    self.balls[i].target_y = Coordinate.THREE_INITIAL[1] + Coordinate.three_coords[i][1] * 11
                self._set_to_centre(Coordinate.three_coords)

    def out(self, screen):
        for ball in self.balls:
            ball.fly_out()
            ball.draw(screen)

    def _set_to_centre(self, coordinate):
        for ball in self.balls[len(coordinate):]:
            ball.in_pos = False
            ball.target_x = Coordinate.CENTRE_OF_SCREEN[0]
            ball.target_y = Coordinate.CENTRE_OF_SCREEN[1]
            ball.x = Coordinate.CENTRE_OF_SCREEN[0]
            ball.y = Coordinate.CENTRE_OF_SCREEN[1]

    def animate_all(self, screen):
        if not self.completed:
            self.animate_1(screen)
            return
        match self.completed[0]:
            case Coordinate.one:
                self.animate_2(screen)
            case Coordinate.two:
                self.animate_3(screen)
