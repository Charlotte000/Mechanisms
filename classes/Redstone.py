import pygame

import classes as c

class Redstone(c.Entity, c.EntityConductor):
    def __init__(self):
        self.state = 0
        super().__init__(0)
    
    def before_update(self, mesh: c.Mesh, x: int, y: int):
        self.current = 0

    def draw(self, screen: pygame.Surface, mesh: c.Mesh, x: int, y: int, size: int):
        screen.blit(Redstone._get_image(mesh, x // size, y // size, size, self._get_color()), (x, y))

    def _get_color(self) -> tuple[int, int, int]:
        return (50 + 200 * self.current, 0, 0)
    
    @staticmethod
    def _get_image(mesh: c.Mesh, x: int, y: int, size: int, color: tuple[int, int, int]):
        img = pygame.Surface((size, size))
        img.set_colorkey((0, 0, 0))
        pygame.draw.circle(img, color, (size // 2 + 1, size // 2), size // 4)
        for dx, dy in c.EntityConductor.CONDUCTOR_RANGE:
            if (item := mesh.get_at(x + dx, y + dy)) and \
                isinstance(item, (c.EntityGenerator, c.EntityConductor, c.EntityConsumer)):
                pygame.draw.line( \
                    img, \
                    color, \
                    (size / 2, size / 2), \
                    (size / 2 + dx * size / 2, size / 2 + dy * size / 2), \
                    size // 4
                )
        return img
