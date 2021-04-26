import pygame, random
import worldClass
pygame.init()

#Variables
simSize = 256
gridSize = 1

simColours = {0: (8, 96, 168), 1: (245, 234, 146),2: (26, 148, 49)}
agentLocation = (0,0)

window = pygame.display.set_mode((simSize * gridSize, simSize * gridSize))
window2 = pygame.display.set_mode((simSize * gridSize, simSize * gridSize))
pygame.display.set_caption("Weird Survival Game")

#World Functions
def DrawWorld(m):
  for y in range(0, simSize):
    for x in range(0, simSize):
      tileType = 0
      value = m[x][y]
      value = 1 - value

      if value < 0.015:
        colour = simColours[0]
      elif value < 0.05:
        colour = simColours[1]
      else:
        colour = simColours[2]
      #simColours[tileType]
      #255 * value, 255 * value, 255 * value
      pygame.draw.rect(window2, (colour), ((x * gridSize), (simSize * gridSize) - (y * gridSize) - gridSize, gridSize, gridSize))
      #pygame.display.update()

world = worldClass.worldMap(simSize)
world.genMap(104)

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