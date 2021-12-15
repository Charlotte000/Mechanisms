if __name__ == 'classes.Solid':
    from classes.Entity import Entity

    class Solid(Entity):
        def update(self, *args, **kwargs):
            pass

        def draw(self, screen, _, x, y, size):
            super().draw(screen, x, y, size, (255, 153, 0))
