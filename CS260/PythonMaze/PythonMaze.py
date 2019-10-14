from Stack import Stack
from Point import Point
import os
import time

#Constants
GO_ANYWHERE = -1
GO_RIGHT = 0
GO_LEFT = 1
GO_UP = 2
GO_DOWN = 3

class Stack_Item(object):
    """location items designed for a stack"""
    def __init__(self, location, direction):
        '''Defines location and direction'''
        self.location = location
        self.direction = direction

    def getLocation(self):
        return self.location

    def getDirection(self):
        return self.direction

file = open("our_maze_2.txt", "r")
maze_ascii = file.read()
maze_array = maze_ascii.split('\n')
direction = GO_RIGHT

def print_screen(player_pos):
    """Prints the current maze with cursor"""
    os.system('cls')
    for y in range(len(maze_array)):
        line = maze_array[y]
        if player_pos.getY()==y:
            line_length = len(line)
            x = player_pos.getX()
            before = ""
            after = ""
            if (x>0):
                before = line[0:x]
            if (x<line_length):
                after = line[x+1:(x+1)+(line_length-x)]          
            print(before + "@" + after)
        else:
            print(line)
    time.sleep(0.1)

def get_outs(dir, x, y):
    """uses cordinates to figure out where the cursor can move"""
    exits = []     
    if (dir!=GO_LEFT):                          
      if( x<len(maze_array[y])):
          if maze_array[y][x+1]=="0" or maze_array[y][x+1]=="X":    #Check right square
              p = Point(x+1,y)
              exits.append(p)
    if (dir!=GO_RIGHT) :
      if (x>0):
          if maze_array[y][x-1]=="0" or maze_array[y][x-1]=="X":   #Check left square
              p = Point(x-1,y)
              exits.append(p)
    if (dir!=GO_DOWN) :
      if (y>0):
          if maze_array[y-1][x]=="0" or maze_array[y-1][x]=="X":    #Check up square
              p = Point(x, y-1)
              exits.append(p)
    if (dir!=GO_UP)   :
      if (y<len(maze_array)):
          if maze_array[y+1][x]=="0" or maze_array[y+1][x]=="X":    #Check down square
              p = Point(x,y+1)
              exits.append(p)

    return exits

def get_direction(current, destination):
   """Compares to locations and returns the direction between them"""
   if destination.getX()==current.getX():
      if destination.getY()>current.getY():
         return GO_DOWN
      else:
         return GO_UP
   if destination.getX()>current.getX():
      return GO_RIGHT
   else:
      return GO_LEFT

def StartMaze(location):
    """Main routine to solve a ascii maze"""
    lost = True
    options = Stack()
    direction = -1
    while lost: 
        if direction==GO_RIGHT:                                    #Moves the cursor (if direction is assigned)
           location=Point(location.getX()+1,location.getY())
        elif direction==GO_LEFT:
           location=Point(location.getX()-1,location.getY())
        elif direction==GO_UP:
            location=Point(location.getX(),location.getY()-1)
        elif direction==GO_DOWN:
            location=Point(location.getX(),location.getY()+1)
        print_screen(location);                                     #Draws the current screen
        if maze_array[location.getY()][location.getX()] == "X":     #Look at current location to see if we found the exit
            lost = False
            print("You found the exit!")
        else:
            exits=get_outs(direction,location.getX(), location.getY())  #Gets all of the locations we can move to next
            if len(exits)==0:
                if options.size()==0:   #This is a error if the maze can not be solved
                    raise ValueError("I dreamt of a nightmarish cafe, underground, with no way out")
                new_direction_item = options.pop()
                location = new_direction_item.getLocation()
                direction = new_direction_item.getDirection()
                print_screen(location);
            elif len(exits)==1:
                direction = get_direction(location, exits[0])
            else:
                options.push(Stack_Item(exits[1],get_direction(location,exits[1])))
                if len(exits)==3:
                    options.push(Stack_Item(exits[2],get_direction(location,exits[2])))
                direction = get_direction(location,exits[0])


if __name__=="__main__":
    StartMaze(Point(0,1))       #Pass location of where to start in the maze