import pygame
from src import organism, world

pygame.init()

# Rozmiary okna i kolory
WIDTH, HEIGHT = 800, 600
BUTTON_WIDTH, BUTTON_HEIGHT = 150, 50
map_bg = (34, 139, 34)  # Tło mapy (zielony)
button_color = (200, 200, 200)
button_hover_color = (170, 170, 170)
text_color = (0, 0, 0)

# Inicjalizacja ekranu
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Symulacja Organizmu")
map = pygame.Surface((WIDTH, HEIGHT - BUTTON_HEIGHT))

# Obiekty gry
world = world.World()
clock = pygame.time.Clock()
run = True

# Font
font = pygame.font.Font(None, 36)

# Dodanie organizmów
world.addOrganism(organism.Wolf(100, 100, world, 1))
world.addOrganism(organism.Sheep(200, 200, world, 2))

# Funkcja do obsługi przycisku
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

# Główna pętla gry
while run:
    tick = clock.tick(10) / 1000.0
    mouse_pos = pygame.mouse.get_pos()
    click = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click = True

    # Obsługa przycisku "Następna tura"
    if draw_button(screen, WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT - BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, "Następna tura", mouse_pos, click):
        print("Przechodzimy do następnej tury!")
        # W tym miejscu możesz dodać logikę dla "następnej tury", np. aktualizację pozycji organizmów
        for org in world.getOrganismList():
            org.pos_x += 10  # Przykładowy ruch organizmu

    # Rysowanie mapy i organizmów
    map.fill(map_bg)
    for org in world.getOrganismList():
        org.draw(map)

    # Aktualizacja ekranu
    screen.blit(map, (0, 0))
    pygame.display.update()