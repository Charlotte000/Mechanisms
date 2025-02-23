from pygame import Surface

import classes as c


class Mesh:
    CELL_SIZE = 20

    def __init__(self, window_size: tuple[int, int]):
        width = window_size[0] // Mesh.CELL_SIZE
        height = window_size[1] // Mesh.CELL_SIZE
        self.mesh: list[list[c.Entity]] = [
            [c.Empty() for _ in range(width)] for _ in range(height)
        ]

    def set_at(self, x: int, y: int, item: c.Entity):
        if self.check_border(x, y):
            self.mesh[y][x] = item

    def check_border(self, x: int, y: int) -> bool:
        return 0 <= x < len(self.mesh[0]) and 0 <= y < len(self.mesh)

    def get_at(self, x: int, y: int) -> c.Entity | None:
        if self.check_border(x, y):
            return self.mesh[y][x]

    def update(self):
        # Pre update
        for x in range(len(self.mesh[0])):
            for y in range(len(self.mesh)):
                if item := self.get_at(x, y):
                    item.before_update(self, x, y)

        # Update
        for x in range(len(self.mesh[0])):
            for y in range(len(self.mesh)):
                if item := self.get_at(x, y):
                    item.update(self, x, y)

                if isinstance(item, c.EntityGenerator):
                    item.update_generator(self, x, y)

        # Post update
        for x in range(len(self.mesh[0])):
            for y in range(len(self.mesh)):
                if item := self.get_at(x, y):
                    item.after_update(self, x, y)

    def draw(self, screen: Surface):
        for x in range(len(self.mesh[0])):
            for y in range(len(self.mesh)):
                if not isinstance(item := self.mesh[y][x], c.Empty):
                    item.draw(
                        screen,
                        self,
                        x * Mesh.CELL_SIZE,
                        y * Mesh.CELL_SIZE,
                        Mesh.CELL_SIZE,
                    )
