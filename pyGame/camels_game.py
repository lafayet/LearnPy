import pygame, sys

from pygame.locals import *
pygame.init()
fpsClock = pygame.time.Clock()

#useful game dimensions
TILESIZE = 40
MAPWIDTH = 9
MAPHEIGHT = 1

recources_path = ''

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
#INVFONT = pygame.font.Font(path + 'Arial.ttf', 24)

#constants representing colors
BLACK = (0,   0,   0  )
BROWN = (153, 76,  0  )
GREEN = (0,   255, 0  )
BLUE  = (0,   0,   255)
GREY  = (120, 120, 120)
RED   = (255, 0,   0  )
WHITE = (255, 255, 255)

#constants representing the different recources
FREE_PLACE  = 0
RED_CAMEL = 1
BLUE_CAMEL = 2

textures =   {
                FREE_PLACE  : pygame.image.load(recources_path + 'nothing.png'),
                RED_CAMEL : pygame.image.load(recources_path + 'red_camel.png').convert_alpha(),
                BLUE_CAMEL : pygame.image.load(recources_path + 'blue_camel.png').convert_alpha()
            }

tilemap = [[FREE_PLACE for w in range(MAPWIDTH)] for h in range (MAPHEIGHT)]
tilemap [0][0] = RED_CAMEL
tilemap [0][8] = BLUE_CAMEL

pygame.display.set_caption("Camel Game v0.1")

class Camel:
    posXY = [0, 0]
    def __init__(self, color):
        self.color = color
    def setPos (self, x, y):
        self.posXY[0] = x
        self.posXY[1] = y
    def getPos (self):
        return self.posXY
    def getX (self):
        return self.posXY[0]
    def getY (self):
        return self.posXY[1]
    def getColor(self):
        return self.color

camelSelected = 0
tileClicked = [100,0]

blueCamel1 = Camel(BLUE_CAMEL)
blueCamel1.setPos (8, 0)
        
while True:
    DISPLAYSURF.fill(GREY)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()           
        elif event.type == MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            tileClicked[0] = mouse_pos[0]//TILESIZE
            tileClicked[1] = mouse_pos[1]//TILESIZE
            print (tileClicked)

    if camelSelected:
        if (tileClicked[0] == blueCamel1.getX()-1) and (tilemap[0][tileClicked[0]] == FREE_PLACE):
               tilemap[0][tileClicked[0]] = blueCamel1.getColor()
               tilemap[0][tileClicked[0]+1] = FREE_PLACE
               blueCamel1.setPos(tileClicked[0],tileClicked[1])
               camelSelected = 0
               tileClicked = [100, 0]
    else:
        camelSelected = blueCamel1.getPos() == tileClicked
        if (camelSelected):
            print ("selected")
    
    
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(textures[tilemap[row][column]],[column*TILESIZE,row*TILESIZE])

    pygame.display.update()
    fpsClock.tick(24)
