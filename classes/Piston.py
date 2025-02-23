from pygame import Surface
from pygame.draw import rect
from pygame.transform import rotate

import classes as c


class Piston(c.Entity, c.EntityConsumer, c.EntityPushable, c.EntityClickable):
    def __init__(self):
        c.EntityPushable.__init__(self)
        self.active = False
        self.image, self.image_active = Piston._init_image(self.direction)

    def before_update(self, mesh: c.Mesh, x: int, y: int):
        self.active = False

    def update_consumer(self, mesh: c.Mesh, x: int, y: int):
        self.active = True
        self.push_forward(mesh, x, y)

    def draw(self, screen: Surface, mesh: c.Mesh, x: int, y: int, size: int):
        if self.active:
            if self.direction == 1 or self.direction == 2:
                screen.blit(self.image_active, (x, y))
            elif self.direction == 3:
                screen.blit(self.image_active, (x - size, y))
            elif self.direction == 0:
                screen.blit(self.image_active, (x, y - size))
        else:
            screen.blit(self.image, (x, y))

    def click(self, button: int):
        self.direction = (self.direction + 1) % 4
        self.image, self.image_active = Piston._init_image(self.direction)

    @staticmethod
    def _init_image(direction: int) -> tuple[Surface, Surface]:
        img = Surface((c.Mesh.CELL_SIZE, c.Mesh.CELL_SIZE))
        img2 = Surface((c.Mesh.CELL_SIZE, c.Mesh.CELL_SIZE * 2))
        rect(img, (100, 100, 100), (0, 0, c.Mesh.CELL_SIZE, c.Mesh.CELL_SIZE))

        img2.set_colorkey((0, 0, 0))
        img2.blit(img, (0, c.Mesh.CELL_SIZE))
        rect(
            img2,
            (77, 56, 0),
            (
                c.Mesh.CELL_SIZE * 0.4,
                c.Mesh.CELL_SIZE * 0.25,
                c.Mesh.CELL_SIZE * 0.2,
                c.Mesh.CELL_SIZE * 0.75,
            ),
        )

        rect(img, (177, 156, 10), (0, 0, c.Mesh.CELL_SIZE, c.Mesh.CELL_SIZE * 0.25))
        rect(img2, (177, 156, 10), (0, 0, c.Mesh.CELL_SIZE, c.Mesh.CELL_SIZE * 0.25))
        if direction == 0:
            return img, img2
        if direction == 1:
            return rotate(img, -90), rotate(img2, -90)
        if direction == 2:
            return rotate(img, 180), rotate(img2, 180)
        if direction == 3:
            return rotate(img, 90), rotate(img2, 90)

        raise ValueError()
