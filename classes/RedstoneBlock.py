from pygame import Surface

import classes as c

class RedstoneBlock(c.Entity, c.EntityGenerator):
    def draw(self, screen: Surface, mesh: c.Mesh, x: int, y: int, size: int):
        c.Entity.draw_rect(screen, x, y, size, (138, 0, 0))
