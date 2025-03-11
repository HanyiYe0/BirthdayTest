import asyncio

class Text:
    """
    A text class that helps with the animations

    === Attributes ===
    x: the x coordinate of the text
    y: the y coordinate of the text
    alpha: the transparency value of the text. 0 is invisible, 255 is fully visible.
    fade_in: whether the text is supposed to fade in or not.
    priority: priority of the text when animation is to be played.
              0 is highest priority and the higher the number the lower the priority
    """
    x: int
    y: int
    alpha: int = 0
    fade_in: bool = True
    priority: int
    def __init__(self, text, x, y, priority):
        self.text = text
        self.x = x
        self.y = y
        self.priority = priority

    def fade(self, fade_speed: int):
        if self.priority == 0:
            if self.fade_in:
                self.alpha += fade_speed
                if self.alpha >= 255:
                    self.alpha = 255
                    self.fade_in = False
            else:
                self.alpha -= fade_speed
                if self.alpha <= 0:
                    self.alpha = 0
                    self.fade_in = True
        else:
            self.priority -= 1

    def reset_priority(self, new_priority: int):
        self.priority = new_priority
