from pygame import Surface
from pygame.draw import rect

import classes as c


class Solid(c.Entity):
    def draw(self, screen: Surface, mesh: c.Mesh, x: int, y: int, size: int):
        rect(screen, (255, 153, 0), (x, y, size, size))
