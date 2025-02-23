from abc import ABC
import pygame

class Entity(ABC):
    def draw(self, screen: pygame.Surface, mesh, x: int, y: int, size: int):
        ''' Draws object on the scene '''
        pass

    def before_update(self, mesh, x: int, y: int):
        pass

    def update(self, mesh, x: int, y: int):
        ''' The function is called every tick in the program '''
        pass

    def after_update(self, mesh, x: int, y: int):
        pass

    def copy(self):
        return self.__class__()

    def is_empty(self):
        return self.__class__.__name__ == 'Empty'
    
    @staticmethod
    def draw_rect(screen: pygame.Surface, x: int, y: int, size: int, color: tuple[int, int, int]):
        pygame.draw.rect( \
            screen, \
            color, \
            (x, y, size, size) \
        )
