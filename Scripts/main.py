import pygame, random
import worldClass
pygame.init()

#Variables
simSize = 256
gridSize = 2

simColours = {0: (8, 96, 168), 1: (245, 234, 146), 2: (26, 148, 49), 3: (136, 140, 141), 4: (96, 103, 107), 5: (255, 250, 250)}
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

      if value < 0.016:
        colour = simColours[0] # Water
      elif value < 0.025:
        colour = simColours[1] # Beach
      elif value < 0.35:
        colour = simColours[2] # Land
      elif value < 0.53:
        colour = simColours[3] # Stone1
      elif value < 0.7:
        colour = simColours[4] # Stone2      
      elif value < 1:
        colour = simColours[5] # Mountain

      #simColours[tileType]
      #255 * value, 255 * value, 255 * value
      pygame.draw.rect(window2, (colour), ((x * gridSize), (y * gridSize) - gridSize, gridSize, gridSize))
      #pygame.display.update()

world = worldClass.worldMap(simSize)
world.genMap(1024)

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