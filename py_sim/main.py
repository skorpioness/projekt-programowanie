import pygame
from src import organism, world

# pygame.init()
# screen = pygame.display.set_mode((400, 400))

# map = pygame.Surface((400, 400))
# map_bg = pygame.Color('#8BC34A')

# clock = pygame.time.Clock()

# run = True

# world = world.World()

# while run:
#     tick = clock.tick(10) / 1000.0

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     map.fill(map_bg)


#     screen.blit(map, (0, 0))

#     pygame.display.update()

# pygame.quit()


world = world.World()
world.addOrganism(organism.Wolf(0, 0, world))
world.addOrganism(organism.Sheep(20, 0, world))
world.addOrganism(organism.Sheep(0, 20, world))

for o in world.liveList:
    o.takeTurn()
