import pygame, random
import worldClass
pygame.init()

#Variables
simSize = 240
gridSize = 4
simColours = {0: (26, 148, 49), 1: (8, 96, 168)}
agentLocation = (0,0)

window = pygame.display.set_mode((simSize * gridSize, simSize * gridSize))
pygame.display.set_caption("Weird Survival Game")

#World Functions
def DrawWorld(m):
  for y in range(0, simSize):
    for x in range(0, simSize):
      tileType = 0
      value = m[x][y]

      if value < 0.05:
        tileType = 1
      else:
        tileType = 0
      #simColours[tileType]
      #255 * value, 255 * value, 255 * value
      pygame.draw.rect(window, (simColours[tileType]), ((x * gridSize), (simSize * gridSize) - (y * gridSize) - gridSize, gridSize, gridSize))

world = worldClass.worldMap(simSize)
world.genMap(100)

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