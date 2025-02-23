''' Minecraft mechanism game '''
import pygame
import classes as c
from typing import Type


def draw_mesh(screen):
    for x in range(0, 500, c.Mesh.CELL_SIZE):
        pygame.draw.line(screen, (20, 20, 20), (x, 0), (x, 500))
    for y in range(0, 500, c.Mesh.CELL_SIZE):
        pygame.draw.line(screen, (20, 20, 20), (0, y), (500, y))


pygame.init()
font = pygame.font.SysFont('pc_cga', c.Mesh.CELL_SIZE)
timer = pygame.time.Clock()

# Init surfaces
window = pygame.display.set_mode((500 + c.Mesh.CELL_SIZE, 500))
menu = pygame.Surface((c.Mesh.CELL_SIZE, window.get_height()))

# Init meshes
mesh = c.Mesh((500, 500))
menu_mesh = c.Mesh(menu.get_size())

BLOCKS: list[Type[c.Entity]] = [c.Button, c.Repeater, c.Lever, c.Piston, c.StickyPiston, c.Redstone, c.RedstoneBlock, c.Solid, c.RedstoneTorch]
for y, item in enumerate(BLOCKS):
    menu_mesh.set_at(0, y, item())

# Cursor
cursor_item = c.Empty()

while True:
    # Key & mouse event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x <= 500:
                mouse_x //= c.Mesh.CELL_SIZE
                mouse_y //= c.Mesh.CELL_SIZE
                if event.button == 3:
                    mesh.set_at(mouse_x, mouse_y, c.Empty())
                else:
                    if (item := mesh.get_at(mouse_x, mouse_y)) is not None:
                        if isinstance(item, c.EntityClickable):
                            item.click(event.button)
                        elif item.is_empty():
                            mesh.set_at(mouse_x, mouse_y, cursor_item.copy())
            else:
                if event.button == 1:
                    cursor_item = (menu_mesh.get_at(0, mouse_y // c.Mesh.CELL_SIZE) or c.Empty()).copy()

    # Update screen
    window.fill((50, 50, 50))
    draw_mesh(window)

    # Update mesh
    mesh.update()

    # Draw mesh
    mesh.draw(window)

    # Draw menu
    menu.fill((100, 100, 100))
    draw_mesh(menu)
    menu_mesh.draw(menu)
    window.blit(menu, (500, 0))

    # Draw item name
    for y in range(len(menu_mesh.mesh)):
        if (item := menu_mesh.get_at(0, y)) and not item.is_empty():
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x > 500:
                text = menu_mesh.get_at(0, mouse_y // c.Mesh.CELL_SIZE).__class__.__name__
                window.blit( \
                    font.render(text, False, (255, 255, 255)), \
                    (500 - font.size(text)[0], mouse_y // c.Mesh.CELL_SIZE * c.Mesh.CELL_SIZE + 2) \
                )

    # Update window
    pygame.display.flip()
    timer.tick(60)
    pygame.display.set_caption(str(round(timer.get_fps())))
