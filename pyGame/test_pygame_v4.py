import pygame, sys
import random
import tkinter

from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
window = tkinter.Tk()
window.geometry = ("300x300")
lbl = tkinter.Label(window, text = "Label")
lbl.pack()


#useful game dimensions
TILESIZE = 40
MAPWIDTH = 20
MAPHEIGHT = 15

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE+60))
#constants representing colors
BLACK = (0,   0,   0  )
BROWN = (153, 76,  0  )
GREEN = (0,   255, 0  )
BLUE  = (0,   0,   255)
GREY  = (120, 120, 120)
RED   = (255, 0,   0  )
WHITE = (255, 255, 255)

INVFONT = pygame.font.Font('Arial.ttf', 24)

cloudx = -200
cloudy = 0

#constants representing the different recources
DIRT  = 0
GRASS = 1
WATER = 2
COAL  = 3
ROCK  = 4
LAVA  = 5
PLAYER= 6
CLOUD = 7

#a dictionary linking recources to colours
textures =   {
                DIRT  : pygame.image.load('dirt.png'),
                GRASS : pygame.image.load('grass.png'),
                WATER : pygame.image.load('water.png'),
                COAL  : pygame.image.load('coal.png'),
                ROCK  : pygame.image.load('rock.png'),
                LAVA  : pygame.image.load('lava.png'),
                PLAYER : pygame.image.load('player.png').convert_alpha(),
                CLOUD : pygame.image.load('cloud.png').convert_alpha()
            }

inventory =   {
                DIRT  : 0,
                GRASS : 0,
                WATER : 0,
                COAL  : 0,
                ROCK  : 0,
                LAVA  : 0
            }

resources = [DIRT, GRASS, WATER, COAL, ROCK, LAVA]
tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range (MAPHEIGHT)]

for h in range(MAPHEIGHT):
    for w in range (MAPWIDTH):
        randomNumber = random.randint(0,15)
        if randomNumber == 0:
            tile = COAL
        elif randomNumber == 1 or randomNumber == 2:
            tile = WATER
        elif randomNumber >= 3 and randomNumber <= 7:
            tile = GRASS
        else:
            tile = DIRT
        tilemap[h][w] = tile
        
#set up the display


playerPos = [0,0]

pygame.display.set_caption("just a test")

while True:
    DISPLAYSURF.fill(GREY)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if (event.key == K_RIGHT) and playerPos[0] < MAPWIDTH-1:
                playerPos[0] += 1
            elif (event.key == K_LEFT) and playerPos[0] > 0:
                playerPos[0] -= 1
            elif (event.key == K_DOWN) and playerPos[1] < MAPHEIGHT-1:
                playerPos[1] += 1
            elif (event.key == K_UP) and playerPos[1] > 0:
                playerPos[1] -= 1
            elif event.key == K_SPACE:
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                inventory[currentTile] +=1
                tilemap[playerPos[1]][playerPos[0]] = DIRT
            elif (event.key == K_1) and inventory[DIRT] > 0:
                inventory[DIRT] -=1
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                tilemap[playerPos[1]][playerPos[0]] = DIRT
                inventory[currentTile] +=1
            elif (event.key == K_2) and inventory[GRASS] > 0:
                inventory[GRASS] -=1
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                tilemap[playerPos[1]][playerPos[0]] = GRASS
                inventory[currentTile] +=1
            elif (event.key == K_3) and inventory[WATER] > 0:
                inventory[WATER] -=1
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                tilemap[playerPos[1]][playerPos[0]] = WATER
                inventory[currentTile] +=1
            elif (event.key == K_4) and inventory[COAL] > 0:
                inventory[COAL] -=1
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                tilemap[playerPos[1]][playerPos[0]] = COAL
                inventory[currentTile] +=1
            
            
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(textures[tilemap[row][column]],[column*TILESIZE,row*TILESIZE])
    DISPLAYSURF.blit(textures[PLAYER],[playerPos[0]*TILESIZE,playerPos[1]*TILESIZE])
    DISPLAYSURF.blit(textures[CLOUD],(cloudx,cloudy))
    cloudx+=1
    if cloudx > MAPWIDTH * TILESIZE:
        cloudy = random.randint(0, MAPHEIGHT*TILESIZE)
        cloudx = -200    
    placePosition = 10
    for item in resources:
            DISPLAYSURF.blit(textures[item],[placePosition, MAPHEIGHT*TILESIZE+10])
            placePosition +=45
            textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
            DISPLAYSURF.blit(textObj,(placePosition, MAPHEIGHT*TILESIZE+10))
            placePosition +=55
    pygame.display.update()
    fpsClock.tick(24)
    
window.mainloop()
