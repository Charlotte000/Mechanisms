from pygame import Surface
from pygame.draw import line, polygon, rect

import classes as c


class Repeater(c.Entity, c.EntityGenerator, c.EntityConsumer, c.EntityClickable):
    def __init__(self):
        self.active = False
        self.direction = 0
        self.delay = 1
        self.history = [False] * self.delay
        super().__init__()

    def draw(self, screen: Surface, mesh: c.Mesh, x: int, y: int, size: int):
        rect(screen, Repeater._get_color(self.delay), (x, y, size, size))

        dx, dy = self._get_delta()
        dx = -dx
        dy = -dy
        line(
            screen,
            (200, 50, 50),
            (x + size / 2 + dx * size / 3, y + size / 2 + dy * size / 3),
            (x + size / 2 - dx * size / 3, y + size / 2 - dy * size / 3),
        )
        polygon(
            screen,
            (200, 50, 50),
            [
                (x + size / 2 - dx * size / 3, y + size / 2 - dy * size / 3),
                (x + size / 2 - dy * size / 3, y + size / 2 - dx * size / 3),
                (x + size / 2 + dy * size / 3, y + size / 2 + dx * size / 3),
            ],
        )

    def before_update(self, mesh: c.Mesh, x: int, y: int):
        self.active = False

    def after_update(self, mesh: c.Mesh, x: int, y: int):
        self.history.append(self.active)
        self.history.pop(0)

    def update_generator(self, mesh: c.Mesh, x: int, y: int):
        dx, dy = self._get_delta()
        if self.history[0]:
            if (item := mesh.get_at(x + dx, y + dy)) is not None:
                if isinstance(item, c.EntityConductor):
                    item.current = 1.0
                    item.update_conductor(mesh, x + dx, y + dy)
                elif isinstance(item, c.EntityConsumer):
                    item.update_consumer(mesh, x + dx, y + dy)

    def update_consumer(self, mesh: c.Mesh, x: int, y: int):
        dx, dy = self._get_delta()
        if item := mesh.get_at(x - dx, y - dy):
            if isinstance(item, c.EntityGenerator) or (
                isinstance(item, c.EntityConductor) and item.current > 0
            ):
                self.active = True

    def click(self, button: int):
        if button == 1:
            self.direction = (self.direction + 1) % 4
        elif button == 2:
            self.delay += 25
            if self.delay > 151:
                self.delay = 1
            self.history = [False] * self.delay

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

    @staticmethod
    def _get_color(delay):
        k = (delay + 50) / (151 + 50)
        return (255 * k, 214 * k, 252 * k)
