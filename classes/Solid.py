from pygame import Surface

import classes as c

class Solid(c.Entity):
    def draw(self, screen: Surface, mesh: c.Mesh, x: int, y: int, size: int):
        c.Entity.draw_rect(screen, x, y, size, (255, 153, 0))
