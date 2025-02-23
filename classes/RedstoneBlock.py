from pygame import Surface
from pygame.draw import rect

import classes as c


class RedstoneBlock(c.Entity, c.EntityGenerator):
    def draw(self, screen: Surface, mesh: c.Mesh, x: int, y: int, size: int):
        rect(screen, (138, 0, 0), (x, y, size, size))
