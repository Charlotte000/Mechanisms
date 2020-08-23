if __name__ == 'classes.Button':
    import pygame
    from classes.Entity import Entity
    from classes.Redstone import Redstone
    from classes.EntityGenerator import EntityGenerator
    from classes.EntityClickable import EntityClickable

    class Button(Entity, EntityGenerator, EntityClickable):
        DELAY = 10

        def __init__(self):
            self.cooldown = 0
            super().__init__()

        def update(self, *args, **kwargs):
            # Signal cooldown
            if self.cooldown > 0:
                self.cooldown -= 1
        
        def update_generator(self, *args, **kwargs):
            if self.cooldown > 0:
                super().update_generator(*args, **kwargs)

        def draw(self, screen, _, x, y, size):
            pygame.draw.rect( \
                screen, \
                (117, 89, 19), \
                (x + size * .25, y + size * .25, size * .5, size * .5) \
            )

        def click(self):
            self.cooldown = Button.DELAY
