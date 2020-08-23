if __name__ == 'classes.EntityGenerator':
    class EntityGenerator:
        GENERATOR_RANGE = ([-1, 0], [1, 0], [0, -1], [0, 1])

        def update_generator(self, mesh, x, y):
            for dx, dy in EntityGenerator.GENERATOR_RANGE:
                if (item := mesh.get_at(x + dx, y + dy)) is not None:
                    if item.is_conductor():
                        item.current = 1
                        item.update_conductor(mesh, x + dx, y + dy)
                    elif item.is_consumer():
                        item.update_consumer(mesh, x + dx, y + dy)
