import pygame, sys

from pygame.locals import *
pygame.init()
fpsClock = pygame.time.Clock()

#useful game dimensions
TILESIZE = 40
MAPWIDTH = 9
MAPHEIGHT = 1

recources_path = 'recources/'

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE+30))
INVFONT = pygame.font.Font(recources_path + 'Arial.ttf', 20)

#constants representing colors
BLACK = (0,   0,   0  )
BROWN = (153, 76,  0  )
GREEN = (0,   255, 0  )
BLUE  = (0,   0,   255)
GREY  = (120, 120, 120)
С_RED   = (255, 0,   0  )
WHITE = (255, 255, 255)

#constants representing the different recources
NOTHING = 0
RED = 1
BLUE = 2
SELECTED = 3

textures =   {
                NOTHING  : pygame.image.load(recources_path + 'nothing.png'),
                RED : pygame.image.load(recources_path + 'red_camel.png').convert_alpha(),
                BLUE : pygame.image.load(recources_path + 'blue_camel.png').convert_alpha(),
                SELECTED: pygame.image.load(recources_path + 'selected.png').convert_alpha()
            }

pygame.display.set_caption("Camel Game")

class Camel:
    x = 0
    skin = NOTHING
    def __init__ (self, x, skin, name):
        self.x = x
        self.skin = skin
        self.name = name

    def __lt__ (self, other):
        result = self.x < other.x
        return result

    def move (self, x, camel_list):
        red = self.skin == RED
        blue = self.skin == BLUE
        
        distance = x - self.x
        move_r_1 = (distance == 1)
        move_r_2 = (distance == 2)
        move_l_1 = (distance == -1)
        move_l_2 = (distance == -2)

        neigh_r_blue = False
        neigh_r_red = False
        neigh2_r_free = False
        neigh_l_blue = False
        neigh_l_red = False
        neigh2_l_free = False
        if move_r_1 or move_r_2:
            neigh_r_blue = camel_list[self.x + 1].skin == BLUE
            neigh_r_red = camel_list[self.x + 1].skin == RED
        if move_r_2:
            neigh2_r_free = camel_list[self.x + 2].skin == NOTHING
        if move_l_1 or move_l_2:
            neigh_l_blue = camel_list[self.x - 1].skin == BLUE
            neigh_l_red = camel_list[self.x - 1].skin == RED
        if move_l_2:
            neigh2_l_free = camel_list[self.x - 2].skin == NOTHING
        
        move = False
        
        if move_r_1 and red and not(neigh_r_blue or neigh_r_red):
            move = True
        elif move_r_2 and red and neigh_r_blue and neigh2_r_free:
            move = True           
        elif move_l_1 and blue and not(neigh_l_blue or neigh_l_red):
            move = True
        elif move_l_2 and blue and neigh_l_red and neigh2_l_free:
            move = True

        if move:
            camel_list[x].x = self.x
            self.x = x
            camel_list.sort()
            #print ("Succesfully moved.")
        #else:
            #print ("Oops! You cannot move it here.")

camelSelected1 = False
camelSelected2 = False
restartHover = False
x1 = -1
x2 = -1
tileClicked = [-1,-1]
mouse_pos = [0.0, 0.0]
textObj1 = INVFONT.render("Restart", True, С_RED, WHITE)
textObj2 = INVFONT.render("Restart", True, BLACK, WHITE)
winMsg = INVFONT.render("You won! Congratulations!", True, BLACK, WHITE)
textX = MAPWIDTH*TILESIZE - 10 - textObj1.get_width()
textY = MAPHEIGHT*TILESIZE+5
click = False
camels = [Camel(0,RED, "RedONE"),
          Camel(1,RED, "RedTWO"),
          Camel(2,RED, "RedTHREE"),
          Camel(3,RED, "RedFOUR"),
          Camel(4,NOTHING, "NoName"),
          Camel(5,BLUE, "BlueONE"),
          Camel(6,BLUE, "BlueTWO"),
          Camel(7,BLUE, "BlueTHREE"),
          Camel(8,BLUE, "BlueFOUR")]
skins = ("Nothing", "Red", "Blue")        
while True:
    DISPLAYSURF.fill(WHITE)
    mouse_pos = pygame.mouse.get_pos()
    click = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()           
        elif event.type == MOUSEBUTTONUP:
            tileClicked[0] = mouse_pos[0]//TILESIZE
            tileClicked[1] = mouse_pos[1]//TILESIZE
            click = True
            #print (tileClicked)

    if (mouse_pos[0] > textX) and (mouse_pos[0] < MAPWIDTH*TILESIZE - 10) and (mouse_pos[1] > textY) and (mouse_pos[1] < MAPHEIGHT*TILESIZE+30) :
        restartHover = True
    else:
        restartHover = False

    if restartHover and click:
        camels = [Camel(0,RED, "RedONE"),
          Camel(1,RED, "RedTWO"),
          Camel(2,RED, "RedTHREE"),
          Camel(3,RED, "RedFOUR"),
          Camel(4,NOTHING, "NoName"),
          Camel(5,BLUE, "BlueONE"),
          Camel(6,BLUE, "BlueTWO"),
          Camel(7,BLUE, "BlueTHREE"),
          Camel(8,BLUE, "BlueFOUR")]
        click = False
    if not camelSelected1 and (tileClicked[0] >= 0 and tileClicked[1] == 0):
        camelSelected1 = True
        x1 = tileClicked[0]
        tileClicked[0] = -1
    if not camelSelected2 and camelSelected1 and (tileClicked[0] >= 0 and tileClicked[1] == 0):
        camelSelected2 = True
        x2 = tileClicked[0]
        tileClicked[0] = -1
    if camelSelected1 and camelSelected2:
        camels[x1].move(x2, camels)
        #for c in camels:
            #print ("Camel number = " + str(c.x) + " it's:" + skins[c.skin] + " it's name: " + c.name)    
        camelSelected1 = False
        camelSelected2 = False
    for c in camels:         
        DISPLAYSURF.blit(textures[c.skin],[c.x*TILESIZE,0])
    if camelSelected1:
        DISPLAYSURF.blit(textures[SELECTED],[x1*TILESIZE,0])
    if restartHover:
        textObj = textObj1
    else:
        textObj = textObj2
    
    DISPLAYSURF.blit(textObj,(textX, textY))
    if camels[0].skin == BLUE and camels[1].skin == BLUE and camels[2].skin == BLUE and camels[3].skin == BLUE and camels[4].skin == NOTHING and camels[5].skin == RED and camels[6].skin == RED and camels[7].skin == RED and camels[8].skin == RED:
        DISPLAYSURF.blit(winMsg,(10, textY))    
    pygame.display.update()
    fpsClock.tick(24)
