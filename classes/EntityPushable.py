if __name__ == 'classes.EntityPushable':
    from classes.Empty import Empty
    from classes.Mesh import Mesh

    class EntityPushable:
        RANGE = 10

        def __init__(self):
            self.direction = 0

        def push_forward(self, mesh: Mesh, x: int, y: int) -> None:
            if self.direction == 0:
                dx, dy = 0, -1
            elif self.direction == 1:
                dx, dy = 1, 0
            elif self.direction == 2:
                dx, dy = 0, 1
            elif self.direction == 3:
                dx, dy = -1, 0

            for stage in range(1, EntityPushable.RANGE + 3):
                if (item := mesh.get_at(x + dx * stage, y + dy * stage)) and item.is_empty():
                    break
            if stage != EntityPushable.RANGE + 2:
                for i in range(stage, 1, -1):
                    mesh.set_at( \
                        x + dx * i, y + dy * i, \
                        mesh.get_at(x + dx * (i - 1), y + dy * (i - 1)) \
                    )
                    mesh.set_at(x + dx * (i - 1), y + dy * (i - 1), Empty())

        def push_back(self, mesh: Mesh, x: int, y: int) -> None:
            if self.direction == 0:
                dx, dy = 0, -1
            elif self.direction == 1:
                dx, dy = 1, 0
            elif self.direction == 2:
                dx, dy = 0, 1
            elif self.direction == 3:
                dx, dy = -1, 0
            if (item := mesh.get_at(x + dx * 2, y + dy * 2)):
                mesh.set_at(x + dx, y + dy, item)
                mesh.set_at(x + dx * 2, y + dy * 2, Empty())
