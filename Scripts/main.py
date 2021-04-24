import pygame

window = pygame.display.set_mode((600,600))
#window.display.flip()

running = True
while running == True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False