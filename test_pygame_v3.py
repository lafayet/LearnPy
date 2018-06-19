import pygame, sys

from pygame.locals import *

#constants representing colors
BLACK = (0,   0,   0  )
BROWN = (153, 76,  0  )
GREEN = (0,   255, 0  )
BLUE  = (0,   0,   255)
GREY  = (120, 120, 120)
RED   = (255, 0,   0  )

#constants representing the different recources
DIRT  = 0
GRASS = 1
WATER = 2
COAL  = 3
ROCK  = 4
LAVA  = 5

#a dictionary linking recources to colours
textures =   {
                DIRT  : pygame.image.load('dirt.png'),
                GRASS : pygame.image.load('grass.png'),
                WATER : pygame.image.load('water.png'),
                COAL  : pygame.image.load('coal.png'),
                ROCK  : pygame.image.load('rock.png'),
                LAVA  : pygame.image.load('lava.png')
            }
tilemap = [
           [GRASS,GRASS,DIRT ,DIRT ,WATER,DIRT ,DIRT ,DIRT ,GRASS,GRASS],
           [GRASS,DIRT ,GRASS,GRASS,WATER,GRASS,GRASS,GRASS,DIRT ,GRASS],
           [DIRT ,GRASS,GRASS,DIRT ,GRASS,WATER,DIRT ,GRASS,GRASS,DIRT ],
           [DIRT ,GRASS,GRASS,GRASS,GRASS,WATER,GRASS,GRASS,GRASS,DIRT ],
           [DIRT ,GRASS,GRASS,GRASS,WATER,GRASS,GRASS,GRASS,GRASS,DIRT ],
           [DIRT ,GRASS,DIRT ,WATER,WATER,WATER,GRASS,DIRT ,GRASS,DIRT ],
           [DIRT ,GRASS,GRASS,WATER,WATER,WATER,DIRT ,GRASS,GRASS,DIRT ],
           [GRASS,DIRT ,ROCK ,ROCK ,WATER,ROCK ,ROCK ,GRASS,DIRT ,GRASS],
           [GRASS,ROCK ,LAVA ,LAVA ,ROCK ,COAL ,COAL ,ROCK ,GRASS,GRASS]
          ]

#useful game dimensions
TILESIZE = 42
MAPWIDTH = 10
MAPHEIGHT = 9

#set up the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

pygame.display.set_caption("just a test")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(textures[tilemap[row][column]],[column*TILESIZE,row*TILESIZE])
    pygame.display.update()
