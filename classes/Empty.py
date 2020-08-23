if __name__ == 'classes.Empty':
    from classes.Entity import Entity

    class Empty(Entity):
        def draw(self, screen, mesh, x, y, size):
            pass

        def update(self, mesh, x, y):
            pass
