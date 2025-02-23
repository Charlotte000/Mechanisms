import pygame

import classes as c

class Lever(c.Entity, c.EntityGenerator, c.EntityClickable):
    def __init__(self):
        self.active = False

    def draw(self, screen: pygame.Surface, mesh: c.Mesh, x: int, y: int, size: int):
        pygame.draw.rect( \
            screen, \
            (255, 245, 0) if self.active else (92, 88, 0), \
            (x + size / 4, y + size / 4, size / 2, size / 2) \
        )
    
    def update_generator(self, mesh: c.Mesh, x: int, y: int):
        if self.active:
            super().update_generator(mesh, x, y)
    
    def click(self, button: int):
        self.active = not self.active