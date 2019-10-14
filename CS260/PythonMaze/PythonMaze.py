from Stack import Stack
from Point import Point

GO_RIGHT = 0
GO_LEFT = 1
GO_UP = 2
GO_DOWN = 3

class Stack_Item(object):

    def __init__(self, location, direction):
        '''Defines location and direction'''
        self.location = location
        self.direction = direction

    def getLocation():
        return self.location

    def getDirection():
        return self.direction

file = open("our_maze.txt", "r")
maze_ascii = file.read()
maze_array = maze_ascii.split('\n')
direction = GO_RIGHT

def get_outs(dir, x, y):
    exits = []
    if dir==GO_RIGHT:
      if y<len(maze_array):
          if maze_array[y+1][x]=="0":   #Check Down square
              p = Point(x,y+1)
              exits.append(p)
      if x<len(maze_array[y]):
          if maze_array[y][x+1]=="0":    #Check right square
              p = Point(x+1,y)
              exits.append(p)
      if y>0:
          if maze_array[y-1][x]=="0":    #Check Up square
              p = Point(x,y-1)
              exits.append(p)
    elif dir==GO_LEFT:
      if y<len(maze_array):
          if maze_array[y+1][x]=="0":   #Check Down square
              p = Point(x,y+1)
              exits.append(p)
      if x>0:
          if maze_array[y][x-1]=="0":    #Check left square
              p = Point(x-1,y)
              exits.append(p)
      if y>0:
          if maze_array[y-1][x]=="0":    #Check Up square
              p = Point(x,y-1)
              exits.append(p)
    elif dir==GO_UP:
      if x>0:
          if maze_array[y][x-1]=="0":   #Check left square
              p = Point(x-1,y)
              exits.append(p)
      if y>0:
          if maze_array[y-1][x]=="0":    #Check up square
              p = Point(y-1, x)
              exits.append(p)
      if x<len(maze_array[y]):
          if maze_array[y][x+1]=="0":    #Check right square
              p = Point(x+1,y)
              exits.append(p)
    elif dir==GO_DOWN:
      if x>0:
          if maze_array[y][x-1]=="0":   #Check left square
              p = Point(x-1,y)
              exits.append(p)
      if y<len(maze_array):
          if maze_array[y+1][x]=="0":    #Check down square
              p = Point(x,y+1)
              exits.append(p)
      if x<len(maze_array[y]):
          if maze_array[y][x+1]=="0":    #Check right square
              p = Point(x+1,y)
              exits.append(p)
    return exits

def get_direction(current, destination):
   if destination.getX()==curent.getX():
      if destination.getY()>current.getY():
         return GO_UP
      else:
         return GO_DOWN
   if destination.getX()<current.getX():
      return GO_LEFT
   else:
      return GO_RIGHT

def StartMaze():
    loc= Point(0,1)  
    lost = True
    options = Stack()
    direction=GO_RIGHT

    while lost:
        if direction==GO_RIGHT:
           loc=Point(loc.getX()+1,loc.getY())
        elif direction==GO_LEFT:
           loc=Point(loc.getX()-1,loc.getY())
        elif direction==GO_UP:
            loc=Point(loc.getX(),loc.getY()-1)
        elif direction==GO_DOWN:
            loc=Point(loc.getX(),loc.getY()+1)

        if maze_array[loc.getY()][loc.getX()] == "X":
            lost = False
        else:
            exits=get_outs(direction,loc.getX(), loc.getY())
            if len(exits)==0:
                #Error check to see if stack is empty, return error, no way out
                new_direction_item = stack.pop()
                loc = new_direction_item.getLocation()
                direction = new_direction_item.getDirection()
            elif len(exits)==1:
                get_direction(loc,exits(0))
                loc = exits(0)
            else:
                options.push(Stack_Item(exits(1),get_direction(loc,exits(1))))
                if exists.size()==2:
                    options.push(Stack_Item(exits(2),get_direction(loc,exits(2))))
                direction = get_direction(loc,exits(0))


if __name__=="__main__":
    StartMaze()