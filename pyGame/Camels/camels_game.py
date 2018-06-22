import pygame, sys

from pygame.locals import *
pygame.init()
pygame.display.set_caption("Camel Game")

TILESIZE = 40 #square tiles, side size in px
MAPTILEWIDTH = 9
MAPTILEHEIGHT = 1
MAPWIDTHPX = MAPTILEWIDTH*TILESIZE
MAPHEIGHTPX = MAPTILEHEIGHT*TILESIZE
BARFORTEXTSPX = 30

recources_path = 'recources/'

#create main screen
DISPLAYSURF = pygame.display.set_mode((MAPWIDTHPX,MAPHEIGHTPX+BARFORTEXTSPX))
#init font
INVFONT = pygame.font.Font(recources_path + 'Arial.ttf', 20)
HLPFONT = pygame.font.Font(recources_path + 'Arial.ttf', 12)
#init fps count
fpsClock = pygame.time.Clock()

#colors
C_BLACK = (0,   0,   0  )
С_RED   = (255, 0,   0  )
C_WHITE = (255, 255, 255)

#game texts
helpMsgStr1 =  "Rounds is camels. Red camels can move only right, blue - left."
helpMsgStr2 = "Camel can move on free space near or jump over other colored"
helpMsgStr3 = "camel if there free space behind it. To win, place blue camels"
helpMsgStr4 = "to left side and red to right side.Restart will reset game."
helpMsgStr5 = "Click to start."

restartTxtHovered = INVFONT.render("Restart", True, С_RED, C_WHITE)
restartTxt = INVFONT.render("Restart", True, C_BLACK, C_WHITE)
winMsg = INVFONT.render("You won! Congratulations!", True, C_BLACK, C_WHITE)

#pygame can't blit multiple line string. So there is five strings for one help message
helpMsg1 = HLPFONT.render(helpMsgStr1, True, C_BLACK, C_WHITE)
helpMsg2 = HLPFONT.render(helpMsgStr2, True, C_BLACK, C_WHITE)
helpMsg3 = HLPFONT.render(helpMsgStr3, True, C_BLACK, C_WHITE)
helpMsg4 = HLPFONT.render(helpMsgStr4, True, C_BLACK, C_WHITE)
helpMsg5 = HLPFONT.render(helpMsgStr5, True, C_BLACK, C_WHITE)

#game text position on screen
textX = MAPWIDTHPX - 10 - restartTxtHovered.get_width()
textY = MAPHEIGHTPX + 5

#camels types
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

class Camel:
    x = 0 #x position of camel
    skin = NOTHING #camel type
    def __init__ (self, x, skin, name):
        self.x = x
        self.skin = skin
        self.name = name

    def __lt__ (self, other):
        result = self.x < other.x
        return result

    # method to move camels if possible
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

# bool flags to control game state
camelSelected1 = False  # camel which will be moved selected flag
camelSelected2 = False  # camel at which place user want to move first camel (free space is also camels)
restartHover = False    # restart text hovered flag
click = False           # mouse click flag
showHelp = True

x1 = -1                 # x position of first camel
x2 = -1                 # x position of second
tileClicked = [-1,-1]
mouse_pos = [0.0, 0.0]

# main game loop      
while True:
    #clear screen with white color
    DISPLAYSURF.fill(C_WHITE)
    mouse_pos = pygame.mouse.get_pos()
    click = False

    #process events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()           
        elif event.type == MOUSEBUTTONUP:
            if not showHelp:
                tileClicked[0] = mouse_pos[0]//TILESIZE
                tileClicked[1] = mouse_pos[1]//TILESIZE
                click = True
            else:
                showHelp = False
            #print (tileClicked)

    #check that restart is hovered
    if (mouse_pos[0] > textX) and (mouse_pos[0] < MAPWIDTHPX - 10) and (mouse_pos[1] > textY) and (mouse_pos[1] < MAPHEIGHTPX+BARFORTEXTSPX) :
        restartHover = True
    else:
        restartHover = False

    #reset game
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

    #define first selected camel
    if not camelSelected1 and (tileClicked[0] >= 0 and tileClicked[1] == 0):
        camelSelected1 = True
        x1 = tileClicked[0]
        tileClicked[0] = -1

    #define second selected camel
    if not camelSelected2 and camelSelected1 and (tileClicked[0] >= 0 and tileClicked[1] == 0):
        camelSelected2 = True
        x2 = tileClicked[0]
        tileClicked[0] = -1

    #move camels
    if camelSelected1 and camelSelected2:
        camels[x1].move(x2, camels)
        #for c in camels:
            #print ("Camel number = " + str(c.x) + " it's:" + skins[c.skin] + " it's name: " + c.name)    
        camelSelected1 = False
        camelSelected2 = False

    #draw camels
    for c in camels:         
        DISPLAYSURF.blit(textures[c.skin],[c.x*TILESIZE,0])

    #draw selection of camel
    if camelSelected1:
        DISPLAYSURF.blit(textures[SELECTED],[x1*TILESIZE,0])

    if restartHover:
        textObj = restartTxtHovered
    else:
        textObj = restartTxt

    #draw restart
    DISPLAYSURF.blit(textObj,(textX, textY))

    #check win condition and show win msg if so
    if camels[0].skin == BLUE and camels[1].skin == BLUE and camels[2].skin == BLUE and camels[3].skin == BLUE and camels[4].skin == NOTHING and camels[5].skin == RED and camels[6].skin == RED and camels[7].skin == RED and camels[8].skin == RED:
        DISPLAYSURF.blit(winMsg,(10, textY))    

    if showHelp:
        DISPLAYSURF.fill(C_WHITE)
        DISPLAYSURF.blit(helpMsg1,(5, 2))
        DISPLAYSURF.blit(helpMsg2,(5, 15))
        DISPLAYSURF.blit(helpMsg3,(5, 28))
        DISPLAYSURF.blit(helpMsg4,(5, 41))
        DISPLAYSURF.blit(helpMsg5,(5, 54))
    #update screen
    pygame.display.update()
    fpsClock.tick(24)
