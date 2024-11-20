import pygame
import random
from py_sim.src.organism import Wolf, Sheep, Lion, Scorpion, Grass, Guarana, Milkweed, Turtle
from src import  world

pygame.init()
def generate_random_organisms(world):
    organisms = []
    for _ in range(20):
        organism_type = random.choice([Wolf, Sheep, Lion, Scorpion, Turtle, Grass, Guarana, Milkweed,])

        pos_x = random.randint(0, 19)*20
        pos_y = random.randint(0, 19)*20

        organism = organism_type(pos_x, pos_y, world, world._next_id)

        world.addOrganism(organism)
        organisms.append(organism)

    return organisms

WIDTH, HEIGHT = 400, 450
BUTTON_WIDTH, BUTTON_HEIGHT = 150, 50
map_bg = (34, 139, 34)
button_color = (200, 200, 200)
button_hover_color = (170, 170, 170)
text_color = (0, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Symulacja Organizmu")
map = pygame.Surface((WIDTH, HEIGHT - BUTTON_HEIGHT))

world = world.World()
generate_random_organisms(world)
clock = pygame.time.Clock()
run = True

# Font
font = pygame.font.Font(None, 36)

def draw_button(screen, x, y, width, height, text, mouse_pos, click):
    if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
        pygame.draw.rect(screen, button_hover_color, (x, y, width, height))
        if click:
            return True
    else:
        pygame.draw.rect(screen, button_color, (x, y, width, height))
    text_surface = font.render(text, True, text_color)
    screen.blit(
        text_surface,
        (
            x + (width - text_surface.get_width()) // 2,
            y + (height - text_surface.get_height()) // 2,
        ),
    )
    return False

while run:
    tick = clock.tick(10) / 1000.0
    mouse_pos = pygame.mouse.get_pos()
    click = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click = True


    if draw_button(screen, WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT - BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT,
                   "Następna tura", mouse_pos, click):
        print("Przechodzimy do następnej tury!")
        world.playTurn()

    map.fill(map_bg)
    for org in world.getOrganismList():
        org.draw(map)

    screen.blit(map, (0, 0))
    pygame.display.flip()