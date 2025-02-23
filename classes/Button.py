from pygame import Surface
from pygame.draw import rect

import classes as c


class Button(c.Entity, c.EntityGenerator, c.EntityClickable):
    DELAY = 10

    def __init__(self):
        self.cooldown = 0

    def update(self, mesh: c.Mesh, x: int, y: int):
        # Signal cooldown
        if self.cooldown > 0:
            self.cooldown -= 1

    def update_generator(self, mesh: c.Mesh, x: int, y: int):
        if self.cooldown > 0:
            super().update_generator(mesh, x, y)

    def draw(self, screen: Surface, mesh: c.Mesh, x: int, y: int, size: int):
        rect(
            screen,
            (117, 89, 19),
            (x + size * 0.25, y + size * 0.25, size * 0.5, size * 0.5),
        )

    def click(self, button: int):
        self.cooldown = Button.DELAY
