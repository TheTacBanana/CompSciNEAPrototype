#Imports
import pygame, random, json, os
from datetime import datetime
import worldClass, agentClass

#Variables
simSize = 128
gridSize = 4
simSeed = 420

#World Functions
def DrawWorld():
  if world.grayscale == False: # Split into an if statement for optimisation, doesnt need to check if its grayscale after drawing every pixel
    for y in range(0, simSize):
      for x in range(0, simSize):
        colour = world.colourArray[x][y]
        pygame.draw.rect(window, (colour), ((x * gridSize), (y * gridSize), gridSize, gridSize))
  else:
    for y in range(0, simSize):
      for x in range(0, simSize):
        value = world.heightArray[x][y]
        pygame.draw.rect(window, (255 * value, 255 * value, 255 * value), ((x * gridSize), (y * gridSize), gridSize, gridSize))

  # Draw Agent
  pygame.draw.rect(window, (255, 140, 0), ((agent.agentLocX * gridSize), (agent.agentLocY * gridSize), gridSize, gridSize))

def RandomWorld():
  SetWorld(random.randint(0, 10000))

def SetWorld(seed):
  #print(datetime.now().time())
  world.genMap(seed)
  #print(datetime.now().time())
  DrawWorld()
  #print(datetime.now().time())

#Setup
window = pygame.display.set_mode((simSize * gridSize, simSize * gridSize))
pygame.display.set_caption("Procedural Generation")

agent = agentClass.agent()
world = worldClass.worldMap(simSize)
#RandomWorld()
SetWorld(420)
agent.updateSurroundings(world.typeArray)

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
      elif event.key == pygame.K_w:
        agent.Move(0)
        agent.updateSurroundings(world.typeArray)
        DrawWorld()
      elif event.key == pygame.K_d:
        agent.Move(1)
        agent.updateSurroundings(world.typeArray)
        DrawWorld()
      elif event.key == pygame.K_s:
        agent.Move(2)
        agent.updateSurroundings(world.typeArray)
        DrawWorld()
      elif event.key == pygame.K_a:
        agent.Move(3)
        agent.updateSurroundings(world.typeArray)
        DrawWorld()

  pygame.display.update()