import pygame

import classes as c

class StickyPiston(c.Entity, c.EntityConsumer, c.EntityPushable, c.EntityClickable):
    def __init__(self):
        c.EntityPushable.__init__(self)
        self._to_push_back = False
        self.active = False
        self.image, self.image_active = StickyPiston._init_image(self.direction)
        super().__init__()

    def before_update(self, mesh: c.Mesh, x: int, y: int):
        if self.active:
            self._to_push_back = True
        self.active = False

    def after_update(self, mesh: c.Mesh, x: int, y: int):
        if self._to_push_back:
            self.push_back(mesh, x, y)
        self._to_push_back = False

    def update_consumer(self, mesh: c.Mesh, x: int, y: int):
        self.active = True
        self._to_push_back = False
        self.push_forward(mesh, x, y)

    def draw(self, screen: pygame.Surface, mesh: c.Mesh, x: int, y: int, size: int):
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
        self.image, self.image_active = StickyPiston._init_image(self.direction)

    @staticmethod
    def _init_image(direction: int) -> tuple[pygame.Surface, pygame.Surface]:
        img = pygame.Surface((c.Mesh.CELL_SIZE, c.Mesh.CELL_SIZE))
        img2 = pygame.Surface((c.Mesh.CELL_SIZE, c.Mesh.CELL_SIZE * 2))
        pygame.draw.rect(img, (100, 100, 100), (0, 0, c.Mesh.CELL_SIZE, c.Mesh.CELL_SIZE))

        img2.set_colorkey((0, 0, 0))
        img2.blit(img, (0, c.Mesh.CELL_SIZE))

        pygame.draw.rect( \
            img2, \
            (77, 56, 0), \
            ( \
                c.Mesh.CELL_SIZE * .4, c.Mesh.CELL_SIZE * .25, \
                c.Mesh.CELL_SIZE * .2, c.Mesh.CELL_SIZE * .75 \
            ) \
        )
        pygame.draw.rect(img, (12, 176, 72), (0, 0, c.Mesh.CELL_SIZE, c.Mesh.CELL_SIZE * .25))
        pygame.draw.rect(img2, (12, 176, 72), (0, 0, c.Mesh.CELL_SIZE, c.Mesh.CELL_SIZE * .25))
        if direction == 0:
            return img, img2
        if direction == 1:
            return pygame.transform.rotate(img, -90), pygame.transform.rotate(img2, -90)
        if direction == 2:
            return pygame.transform.rotate(img, 180), pygame.transform.rotate(img2, 180)
        if direction == 3:
            return pygame.transform.rotate(img, 90), pygame.transform.rotate(img2, 90)

        raise ValueError()