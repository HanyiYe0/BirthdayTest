class Text:
    x: int
    y: int
    alpha: int = 0
    fade_in: bool = True

    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y

    def fade(self, fade_speed: int):
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
