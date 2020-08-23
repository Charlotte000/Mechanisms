if __name__ == 'classes.Piston':
    import pygame
    from classes.Entity import Entity
    from classes.EntityConsumer import EntityConsumer
    from classes.EntityPushable import EntityPushable
    from classes.EntityClickable import EntityClickable
    from classes.Mesh import Mesh

    class Piston(Entity, EntityConsumer, EntityPushable, EntityClickable):
        def __init__(self):
            EntityPushable.__init__(self)
            self.active = False
            self.image, self.image_active = Piston._init_image(self.direction)
            super().__init__()

        def update(self, *args, **kwargs):
            pass

        def before_update(self, *args, **kwargs):
            self.active = False

        def update_consumer(self, mesh, x, y):
            self.active = True
            self.push_forward(mesh, x, y)

        def draw(self, screen, _, x, y, size):
            if self.active:
                if self.direction == 1 or self.direction == 2:
                    screen.blit(self.image_active, (x, y))
                elif self.direction == 3:
                    screen.blit(self.image_active, (x - size, y))
                elif self.direction == 0:
                    screen.blit(self.image_active, (x, y - size))
            else:
                screen.blit(self.image, (x, y))

        def click(self):
            self.direction += 1
            if self.direction > 3:
                self.direction = 0
            self.image, self.image_active = Piston._init_image(self.direction)

        @staticmethod
        def _init_image(direction):
            img = pygame.Surface((Mesh.CELL_SIZE, Mesh.CELL_SIZE))
            img2 = pygame.Surface((Mesh.CELL_SIZE, Mesh.CELL_SIZE * 2))
            img2.fill((50, 50, 50))
            pygame.draw.rect(img, (100, 100, 100), (0, 0, Mesh.CELL_SIZE, Mesh.CELL_SIZE))

            half_size = Mesh.CELL_SIZE / 2
            pygame.draw.line( \
                img, \
                (255, 50, 50), \
                (half_size, Mesh.CELL_SIZE), \
                (half_size, 0), \
            )
            pygame.draw.polygon( \
                img, \
                (255, 50, 50), \
                [ \
                    (half_size * .5, half_size), \
                    (half_size, 0), \
                    (half_size * 1.5, half_size)], \
            )
            img2.blit(img, (0, Mesh.CELL_SIZE))
            pygame.draw.polygon( \
                img2, \
                (77, 56, 0), \
                ( \
                    [0, 0], \
                    [Mesh.CELL_SIZE, 0], \
                    [Mesh.CELL_SIZE, Mesh.CELL_SIZE * .25], \
                    [Mesh.CELL_SIZE * .6, Mesh.CELL_SIZE * .25], \
                    [Mesh.CELL_SIZE * .6, Mesh.CELL_SIZE], \
                    [Mesh.CELL_SIZE * .4, Mesh.CELL_SIZE], \
                    [Mesh.CELL_SIZE * .4, Mesh.CELL_SIZE * .25], \
                    [0, Mesh.CELL_SIZE * .25], \
                ) \
            )
            if direction == 0:
                return img, img2
            if direction == 1:
                return pygame.transform.rotate(img, -90), pygame.transform.rotate(img2, -90)
            if direction == 2:
                return pygame.transform.rotate(img, 180), pygame.transform.rotate(img2, 180)
            if direction == 3:
                return pygame.transform.rotate(img, 90), pygame.transform.rotate(img2, 90)
