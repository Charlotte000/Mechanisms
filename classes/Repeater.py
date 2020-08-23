if __name__ == 'classes.Repeater':
    import pygame
    from classes.Entity import Entity
    from classes.EntityGenerator import EntityGenerator
    from classes.EntityConsumer import EntityConsumer
    from classes.EntityConductor import EntityConductor
    from classes.EntityClickable import EntityClickable

    class Repeater(Entity, EntityGenerator, EntityConsumer, EntityClickable):
        def __init__(self):
            self.active = False
            self.ignore = None
            self.delay = 1
            self.history = [None] * self.delay
            super().__init__()

        def draw(self, screen, _, x, y, size):
            super().draw(screen, x, y, size, Repeater._get_color(self.delay))
            if self.ignore:
                pygame.draw.line( \
                    screen, \
                    (200, 50, 50), \
                    (x + size / 2 + self.ignore[0] * size / 3, y + size / 2 + self.ignore[1] * size / 3), \
                    (x + size / 2 - self.ignore[0] * size / 3, y + size / 2 - self.ignore[1] * size / 3)
                )
                pygame.draw.polygon( \
                    screen, \
                    (200, 50, 50), \
                    [ \
                        (x + size / 2 - self.ignore[0] * size / 3, y + size / 2 - self.ignore[1] * size / 3), \
                        (x + size / 2 - self.ignore[1] * size / 3, y + size / 2 - self.ignore[0] * size / 3), \
                        (x + size / 2 + self.ignore[1] * size / 3, y + size / 2 + self.ignore[0] * size / 3), \
                    ] \
                )

        def before_update(self, mesh, x, y):
            self.active = False

        def update(self, mesh, x, y):
            pass

        def after_update(self, mesh, x, y):
            self.history.append(self.active)
            self.history.pop(0)

        def update_generator(self, mesh, x, y):
            if self.history[0]:
                dx, dy = [-self.ignore[0], -self.ignore[1]]
                if (item := mesh.get_at(x + dx, y + dy)) is not None:
                    if item.is_conductor():
                        item.current = 1
                        item.update_conductor(mesh, x + dx, y + dy)
                    elif item.is_consumer():
                        item.update_consumer(mesh, x + dx, y + dy)

        def update_consumer(self, mesh, x, y):
            cons_range = list(EntityConductor.CONDUCTOR_RANGE)
            if self.ignore:
                cons_range.remove([-self.ignore[0], -self.ignore[1]])
            for dx, dy in cons_range:
                if (item := mesh.get_at(x + dx, y + dy)):
                    if item.is_generator() or (item.is_conductor() and item.current > 0):
                        self.ignore = [dx, dy]
                        self.active = True

        def click(self):
            self.delay += 25
            if self.delay > 151:
                self.delay = 1
            self.history = [None] * self.delay

        @staticmethod
        def _get_color(delay):
            k = (delay + 50) / (151 + 50)
            return (255 * k, 214 * k, 252 * k)
