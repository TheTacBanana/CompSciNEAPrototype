import pygame, random
import worldClass
pygame.init()

#Variables
simSize = (60,60)
simGrid = [[0 for i in range(60)] for j in range(60)]
simColours = {0: (26, 148, 49), 1: (8, 96, 168)}
agentLocation = (0,0)

worldSeed = 0

window = pygame.display.set_mode((simSize[0] * 8, simSize[1] * 8))
pygame.display.set_caption("Weird Survival Game")

#World Functions
def DrawWorld(m):
  for y in range(0, 60):
    for x in range(0, 60):
      pygame.draw.rect(window, simColours[m[x][y]], ((x * 8), m(y * 8), 8, 8))

world = worldClass.worldMap(60)

#print(world.name)
world.genMap()

DrawWorld(world.mapArray)

#Main loop
running = True
while running == True:
  #window.fill((26, 148, 49))
  #DrawWorld(simGrid)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  pygame.display.update()

