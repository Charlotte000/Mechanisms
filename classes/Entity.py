from abc import ABC

from pygame import Surface

import classes as c


class Entity(ABC):
    def draw(self, screen: Surface, mesh: "c.Mesh", x: int, y: int, size: int):
        """Draws object on the scene"""
        pass

    def before_update(self, mesh: "c.Mesh", x: int, y: int):
        pass

    def update(self, mesh: "c.Mesh", x: int, y: int):
        """The function is called every tick in the program"""
        pass

    def after_update(self, mesh: "c.Mesh", x: int, y: int):
        pass

    def copy(self):
        return self.__class__()
