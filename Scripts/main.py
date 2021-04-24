import pygame, random
pygame.init()

import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

#Variables
simSize = (60,60)
simGrid = [[0 for i in range(60)] for j in range(60)]
simColours = {0: (26, 148, 49), 1: (8, 96, 168)}
agentLocation = (0,0)

worldSeed = 0

window = pygame.display.set_mode((simSize[0] * 8, simSize[1] * 8))
pygame.display.set_caption("Weird Survival Game")


simGrid[58][58] = 1
#simGrid[1][59] = 1

#Functions
def GenWorld():
  for y in range(0, 60):
    for x in range(0, 60):
      simGrid[x][y] = random.randint(0,1)

def DrawWorld(m):
  for y in range(0, 60):
    for x in range(0, 60):
      pygame.draw.rect(window, simColours[simGrid[x][y]], ((x * 8), (y * 8), 8, 8))

GenWorld()
DrawWorld(simGrid)

#Main loop
running = True
while running == True:
  #window.fill((26, 148, 49))
  #DrawWorld(simGrid)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  pygame.display.update()

