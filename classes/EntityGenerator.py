import classes as c


class EntityGenerator:
    GENERATOR_RANGE = ([-1, 0], [1, 0], [0, -1], [0, 1])

    def update_generator(self, mesh: "c.Mesh", x: int, y: int):
        for dx, dy in EntityGenerator.GENERATOR_RANGE:
            if (item := mesh.get_at(x + dx, y + dy)) is not None:
                if isinstance(item, c.EntityConductor):
                    item.current = 1.0
                    item.update_conductor(mesh, x + dx, y + dy)
                elif isinstance(item, c.EntityConsumer):
                    item.update_consumer(mesh, x + dx, y + dy)
