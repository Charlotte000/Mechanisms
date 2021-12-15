if __name__ == 'classes.Redstone':
    import pygame
    
    from classes.Entity import Entity
    from classes.EntityConductor import EntityConductor

    class Redstone(Entity, EntityConductor):
        def __init__(self):
            self.state = 0
            super().__init__()
            EntityConductor.__init__(self, 0)

        def update(self, mesh, x, y):
            pass

        def before_update(self, *args, **kwargs):
            self.current = 0

        def draw(self, screen, mesh, x, y, size):
            screen.blit(Redstone._get_image(mesh, x // size, y // size, size, self._get_color()), (x, y))

        def _get_color(self):
            return (50 + 200 * self.current, 0, 0)
        
        @staticmethod
        def _get_image(mesh, x, y, size, color):
            img = pygame.Surface((size, size))
            img.set_colorkey((0, 0, 0))
            pygame.draw.circle(img, color, (size // 2 + 1, size // 2), size // 4)
            for dx, dy in EntityConductor.CONDUCTOR_RANGE:
                if (item := mesh.get_at(x + dx, y + dy)) and \
                    (item.is_generator() or item.is_conductor() or item.is_consumer()):
                    pygame.draw.line( \
                        img, \
                        color, \
                        (size / 2, size / 2), \
                        (size / 2 + dx * size / 2, size / 2 + dy * size / 2), \
                        size // 4
                    )
            return img
