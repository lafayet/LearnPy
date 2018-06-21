import pygame, sys

from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((300,300))

pygame.display.set_caption("just a test")

bg = [[0,0,1,1,1,1,1,1,0,0],
      [0,1,0,0,0,0,0,0,1,0],
      [1,0,0,1,0,0,1,0,0,1],
      [1,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,1],
      [1,0,1,0,0,0,0,1,0,1],
      [1,0,0,1,1,1,1,0,0,1],
      [0,1,0,0,0,0,0,0,1,0],
      [0,0,1,1,1,1,1,1,0,0]]
i = 50
k = 50


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    for c in bg:
        for r in c:
            if r == 1:
                pygame.draw.rect(DISPLAYSURF, (0,255,0), [k,i,20,20])
            k += 20
        k = 50
        i += 20
    i = 50
    k = 50
    pygame.display.update()
