if __name__ == 'classes.Entity':
    import pygame

    class Entity:
        def __init__(self):
            pass

        def draw(self, screen, x, y, size, color):
            ''' Draws object on the scene '''
            pygame.draw.rect( \
                screen, \
                color, \
                (x, y, size, size) \
            )

        def before_update(self, *args, **kwargs):
            pass

        def update(self, *args, **kwargs):
            ''' The function is called every tick in the program '''
            raise NotImplementedError

        def after_update(self, *args, **kwargs):
            pass

        def copy(self):
            return self.__class__()

        def is_empty(self):
            return self.__class__.__name__ == 'Empty'

        def is_generator(self):
            return 'EntityGenerator' in [cl.__name__ for cl in self.__class__.__bases__]

        def is_conductor(self):
            return 'EntityConductor' in [cl.__name__ for cl in self.__class__.__bases__]

        def is_consumer(self):
            return 'EntityConsumer' in [cl.__name__ for cl in self.__class__.__bases__]

        def is_clickable(self):
            return 'EntityClickable' in [cl.__name__ for cl in self.__class__.__bases__]
