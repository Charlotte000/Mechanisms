if __name__ == 'classes.EntityConsumer':
    from classes.Mesh import Mesh

    class EntityConsumer:
        def update_consumer(self, mesh: Mesh, x: int, y: int) -> None:
            raise NotImplementedError
