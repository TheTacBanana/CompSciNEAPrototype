import pygame, random
import worldClass
pygame.init()

#Variables
simSize = (60,60)
simColours = {0: (26, 148, 49), 1: (8, 96, 168)}
agentLocation = (0,0)

window = pygame.display.set_mode((simSize[0] * 8, simSize[1] * 8))
pygame.display.set_caption("Weird Survival Game")

#World Functions
def DrawWorld(m):
  for y in range(0, 60):
    for x in range(0, 60):
      tileType = 0
      value = m[x][y]

      if value < 0.7:
        tileType = 0
      else:
        tileType = 1
      pygame.draw.rect(window, (255 * value, 255 * value, 255 * value), ((x * 8), (simSize[1] * 8) - (y * 8) - 8, 8, 8))

world = worldClass.worldMap(60)
world.genMap(69)

#print(world.mapArray)
DrawWorld(world.mapArray)

#Main loop
running = True
while running == True:
  #DrawWorld(simGrid)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  pygame.display.update()