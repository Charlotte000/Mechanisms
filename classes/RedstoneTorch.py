from pygame import Surface
from pygame.draw import rect

import classes as c


class RedstoneTorch(c.Entity, c.EntityGenerator):
    def __init__(self):
        self.direction = -1
        self.active = True

    def after_update(self, mesh: c.Mesh, x: int, y: int):
        self.active = True
        for i, (dx, dy) in enumerate(((0, -1), (1, 0), (0, 1), (-1, 0))):
            if type(mesh.get_at(x + dx, y + dy)) == c.Solid:
                self.direction = i

                if item := mesh.get_at(x + dx * 2, y + dy * 2):
                    if isinstance(item, c.EntityGenerator) or (
                        isinstance(item, c.EntityConductor) and item.current > 0
                    ):
                        self.active = False
                break
        else:
            self.direction = -1

    def update_generator(self, mesh: c.Mesh, x: int, y: int):
        if self.active:
            super().update_generator(mesh, x, y)

    def draw(self, screen: Surface, mesh: c.Mesh, x: int, y: int, size: int):
        if self.direction != -1:
            dx, dy = self._get_delta()
            rect(
                screen,
                (255, 153, 0),
                (
                    x + size * 0.25 + dx * size * 0.25,
                    y + size * 0.25 + dy * size * 0.25,
                    size * 0.5,
                    size * 0.5,
                ),
            )

        rect(
            screen,
            (250, 0, 0) if self.active else (50, 0, 0),
            (x + size * 0.25, y + size * 0.25, size * 0.5, size * 0.5),
        )

    def _get_delta(self) -> tuple[int, int]:
        return (
            (0, -1)
            if self.direction == 0
            else (
                (1, 0)
                if self.direction == 1
                else (0, 1) if self.direction == 2 else (-1, 0)
            )
        )
