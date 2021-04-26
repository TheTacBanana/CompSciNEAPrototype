#Imports
import pygame, random, json, os
from datetime import datetime
import worldClass

#Variables
simSize = 256
gridSize = 1
simSeed = 420

#World Functions
def DrawWorld(m):
  if world.grayscale == False:
    for y in range(0, simSize):
      for x in range(0, simSize):
        colour = world.typeArray[x][y]
        pygame.draw.rect(window, (colour), ((x * gridSize), (y * gridSize) - gridSize, gridSize, gridSize))
  else:
    for y in range(0, simSize):
      for x in range(0, simSize):
        value = world.heightArray[x][y]
        pygame.draw.rect(window, (255 * value, 255 * value, 255 * value), ((x * gridSize), (y * gridSize) - gridSize, gridSize, gridSize))

def RandomWorld():
  SetWorld(random.randint(0, 10000))

def SetWorld(seed):
  print(datetime.now())
  world.genMap(seed)
  DrawWorld(world.heightArray)
  print(datetime.now())

#Setup
window = pygame.display.set_mode((simSize * gridSize, simSize * gridSize))
pygame.display.set_caption("Procedural Generation")

world = worldClass.worldMap(simSize)
RandomWorld()
#SetWorld(420)

#Main loop
running = True
while running == True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RETURN:
        RandomWorld()
      elif event.key == pygame.K_F2:
        pygame.image.save(window,"DevelopmentScreenshots\\screenshot{}.png".format(len(next(os.walk("DevelopmentScreenshots"))[2])))

  pygame.display.update()