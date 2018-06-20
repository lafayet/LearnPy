NOTHING = 0
RED = 1
BLUE = 2

unit_types = {
    NOTHING : "Nothing",
    RED : "Red",
    BLUE : "Blue"
    }

class Unit:
    unit_type = unit_types[NOTHING]
    selected = 0
    posXY = [-1, -1]
    def __init__(self, pos):
        self.posXY = pos 
        
    def setX (self, x):
        self.posXY[0] = x
    def setY (self, y):
        self.posXY[1] = y
    def setPos (self, pos):
        self.posXY = pos
        
    def getX (self):
        return self.posXY[0]
    def getY (self):
        return self.posXY[1]
    def getPos (self):
        return self.posXY

    def select (self):
        selected = 1
    def deselect (self):
        selected = 0

class Camel (Unit):
    def move (self, other):
        move = 0
        if other.unit_type == unit_types[NOTHING]:
            if self.unit_type == unit_types[BLUE]:
                if (other.getX() == self.getX() - 1) or (other.getX() == self.getX() - 2):
                    move = 1
            else:
                if (other.getX() == self.getX() + 1) or (other.getX() == self.getX() + 2):
                    move = 1
            if move:
                posXY = self.posXY
                self.posXY = other.posXY
                other.posXY = posXY
            else:
                print("can't move")

class BlueCamel (Camel):
    unit_type = unit_types[BLUE]

class RedCamel (Camel):
    unit_type = unit_types[RED]

units = [RedCamel([0,0]),
         RedCamel([1,0]),
         Unit([2,0]),
         BlueCamel([3,0]),
         BlueCamel([4,0])]
run = 1

while (run):
    for u in units:
        print ("type: " + u.unit_type + " pos: " + str(u.getX()))
    
    select = int(input ("pos to select?"))
    move = int(input ("pos to move?"))
    for u in units:
        if u.getX() == select:
            u.move(
##
##    for u in units:
##        print ("type: " + str(u.unit_type) + " pos: " + str(u.getX()))
##    
    run = int(input ("proceed?"))
    



