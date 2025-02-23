import classes as c

class EntityConductor:
    CONDUCTOR_RANGE = ([-1, 0], [1, 0], [0, -1], [0, 1])

    def __init__(self, current):
        self.current = current

    def update_conductor(self, mesh: 'c.Mesh', x: int, y: int):
        for dx, dy in EntityConductor.CONDUCTOR_RANGE:
            if (item := mesh.get_at(x + dx, y + dy)):
                if isinstance(item, EntityConductor) and item.current < self.current - .05:
                    item.current = self.current - .05
                    item.update_conductor(mesh, x + dx, y + dy)
                elif isinstance(item, c.EntityConsumer):
                    item.update_consumer(mesh, x + dx, y + dy)
