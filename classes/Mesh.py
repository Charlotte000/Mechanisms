if __name__ == 'classes.Mesh':
    from pygame import Surface
    
    from classes.Entity import Entity
    from classes.Empty import Empty
    from classes.Entity import Entity

    class Mesh:
        CELL_SIZE = 20

        def __init__(self, window_size):
            width = window_size[0] // Mesh.CELL_SIZE
            height = window_size[1] // Mesh.CELL_SIZE
            self.mesh = [[Empty() for _ in range(width)] for _ in range(height)]

        def set_at(self, x: int, y: int, item: Entity) -> None:
            if self.check_border(x, y):
                self.mesh[y][x] = item

        def check_border(self, x: int, y: int) -> bool:
            return 0 <= x < len(self.mesh[0]) and 0 <= y < len(self.mesh)

        def get_at(self, x: int, y: int) -> Entity:
            if self.check_border(x, y):
                return self.mesh[y][x]

        def update(self) -> None:
            for x in range(len(self.mesh[0])):
                for y in range(len(self.mesh)):
                    self.get_at(x, y).before_update(self, x, y)
      
            for x in range(len(self.mesh[0])):
                for y in range(len(self.mesh)):
                    item = self.get_at(x, y)
                    item.update(self, x, y)
                    if item.is_generator():
                        item.update_generator(self, x, y)

            for x in range(len(self.mesh[0])):
                for y in range(len(self.mesh)):
                    self.get_at(x, y).after_update(self, x, y)

        def draw(self, screen: Surface) -> None:
            for x in range(len(self.mesh[0])):
                for y in range(len(self.mesh)):
                    if not (item := self.mesh[y][x]).is_empty():
                        item.draw(screen, self, x * Mesh.CELL_SIZE, y * Mesh.CELL_SIZE, Mesh.CELL_SIZE)
