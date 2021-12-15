if __name__ == 'classes.Lever':
    import pygame
    
    from classes.Entity import Entity
    from classes.EntityGenerator import EntityGenerator
    from classes.EntityClickable import EntityClickable

    class Lever(Entity, EntityGenerator, EntityClickable):
        def __init__(self):
            self.active = False
        def update(self, mesh, x, y):
            pass

        def draw(self, screen, _, x, y, size):
            pygame.draw.rect( \
                screen, \
                (255, 245, 0) if self.active else (92, 88, 0), \
                (x + size / 4, y + size / 4, size / 2, size / 2) \
            )

        def update_generator(self, mesh, x, y):
            if self.active:
                super().update_generator(mesh, x, y)
        
        def click(self):
            self.active = not self.active