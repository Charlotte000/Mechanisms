''' Minecraft mechanism game '''
import pygame
from classes.Mesh import Mesh
from classes.Solid import Solid
from classes.Piston import Piston
from classes.StickyPiston import StickyPiston
from classes.Redstone import Redstone
from classes.RedstoneBlock import RedstoneBlock
from classes.Button import Button
from classes.Empty import Empty
from classes.Repeater import Repeater
from classes.Lever import Lever


def draw_mesh(screen):
    for x in range(0, 500, Mesh.CELL_SIZE):
        pygame.draw.line(screen, (20, 20, 20), (x, 0), (x, 500))
    for y in range(0, 500, Mesh.CELL_SIZE):
        pygame.draw.line(screen, (20, 20, 20), (0, y), (500, y))


pygame.init()
font = pygame.font.SysFont('pc_cga', Mesh.CELL_SIZE)
timer = pygame.time.Clock()

# Init surfaces
window = pygame.display.set_mode((500 + Mesh.CELL_SIZE, 500))
menu = pygame.Surface((Mesh.CELL_SIZE, window.get_height()))

# Init meshes
mesh = Mesh((500, 500))
menu_mesh = Mesh(menu.get_size())
for y, item in enumerate([Button(), Repeater(), Lever(), Piston(), StickyPiston(), Redstone(), RedstoneBlock(), Solid()]):
    menu_mesh.set_at(0, y, item)

# Cursor
cursor_item = Empty()

while True:
    # Key & mouse event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x <= 500:
                mouse_x //= Mesh.CELL_SIZE
                mouse_y //= Mesh.CELL_SIZE
                if event.button == 1:
                    if (item := mesh.get_at(mouse_x, mouse_y)) is not None:
                        if item.is_clickable():
                            item.click()
                        elif item.is_empty():
                            mesh.set_at(mouse_x, mouse_y, cursor_item.copy())
                if event.button == 3:
                    mesh.set_at(mouse_x, mouse_y, Empty())
            else:
                if event.button == 1:
                    cursor_item = menu_mesh.get_at(0, mouse_y // Mesh.CELL_SIZE).copy()

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
                text = menu_mesh.get_at(0, mouse_y // Mesh.CELL_SIZE).__class__.__name__
                window.blit( \
                    font.render(text, False, (255, 255, 255)), \
                    (500 - font.size(text)[0], mouse_y // Mesh.CELL_SIZE * Mesh.CELL_SIZE + 2) \
                )

    # Update window
    pygame.display.flip()
    timer.tick(60)
    pygame.display.set_caption(str(round(timer.get_fps())))
