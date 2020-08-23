if __name__ == 'classes.RedstoneBlock':
    import pygame
    from classes.Entity import Entity
    from classes.EntityGenerator import EntityGenerator

    class RedstoneBlock(Entity, EntityGenerator):
        def update(self, mesh, x, y):
            pass

        def draw(self, screen, _, x, y, size):
            super().draw(screen, x, y, size, (138, 0, 0))
