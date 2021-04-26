import pygame, random, json
import worldClass
pygame.init()

#Variables
simSize = 256
gridSize = 2
simSeed = 420

simColours = {0: (8, 96, 168), 1: (245, 234, 146), 2: (26, 148, 49), 3: (136, 140, 141), 4: (96, 103, 107), 5: (255, 250, 250)}
agentLocation = (0,0)

window = pygame.display.set_mode((simSize * gridSize, simSize * gridSize))
window2 = pygame.display.set_mode((simSize * gridSize, simSize * gridSize))
pygame.display.set_caption("Weird Survival Game")

#World Functions
def DrawWorld(m):
  if world.grayscale == False:
    for y in range(0, simSize):
      for x in range(0, simSize):
        colour = world.typeArray[x][y]
        pygame.draw.rect(window2, (colour), ((x * gridSize), (y * gridSize) - gridSize, gridSize, gridSize))
  else:
    for y in range(0, simSize):
      for x in range(0, simSize):
        value = world.heightArray[x][y]
        pygame.draw.rect(window2, (255 * value, 255 * value, 255 * value), ((x * gridSize), (y * gridSize) - gridSize, gridSize, gridSize))

def RandomWorld():
  world.genMap(random.randint(0, 10000))
  DrawWorld(world.heightArray)

#Setup
world = worldClass.worldMap(simSize)

#Main loop
running = True
while running == True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RETURN:
        RandomWorld()

  pygame.display.update()