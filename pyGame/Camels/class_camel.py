#camels types
NOTHING = 0
RED = 1
BLUE = 2
SELECTED = 3

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
 
