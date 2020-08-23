if __name__ == 'classes.EntityConductor':
    class EntityConductor:
        CONDUCTOR_RANGE = ([-1, 0], [1, 0], [0, -1], [0, 1])

        def __init__(self, current):
            self.current = current

        def update_conductor(self, mesh, x, y):
            for dx, dy in EntityConductor.CONDUCTOR_RANGE:
                if (item := mesh.get_at(x + dx, y + dy)):
                    if item.is_conductor() and item.current < self.current - .05:
                        item.current = self.current - .05
                        item.update_conductor(mesh, x + dx, y + dy)
                    elif item.is_consumer():
                        item.update_consumer(mesh, x + dx, y + dy)
