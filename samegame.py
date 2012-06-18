#######################
#asmaa.magdi@gmail.com#
#######################


import random
import sys

MAX_COLORS = 6

class SameGame:
    
    def __init__(self, *args, **kwargs):

        self.grid = []
        self.r = 0
        self.c = 0
        self.x = 0
        
        #default constructor.
        #do nothing
        if len(args) == 0:
            pass

        #passing the list to the constructor as the only parameter
        elif len(args) == 1:
            self.grid = args[0]
            self.r = len(self.grid)
            if r > 0:
                self.c = len(self.grid[0])

        #passing the rows and columns of the grid
        elif len(args) == 2:
            self.r = args[0]
            self.c = args[1]

        #passing the rows, columns and number of colors
        elif len(args) == 3:
            self.r = args[0]
            self.c = args[1]
            self.x = args[2]

            if self.x > MAX_COLORS:
                self.x = MAX_COLORS
            
            #I can now generate a random grid
            self.initGame()

    """
    Initializes a random same game grid
    r: number of rows
    c: number of columns
    x: number of different colors
    """
    def initGame(self):
        if self.r == 0 or self.c == 0 or self.x == 0:
            print('Could not initialize game. Please set the number of rows, columns and colors to proceed.')
            return

        #clear grid
        self.grid = []

        for i in range(0, self.r):
            row = []
            for j in range(0, self.c):
                row.append(random.randint(0, self.x - 1))
            self.grid.append(row)

    """
    Finds a connected region from a seed point
    Used to determine how many (and which) cells to remove, if any, when the user clicks on a cell (y, x)
    Based of a BFS algorithm
    """
    def connectedRegion(self, y, x):
        
        if self.grid[y][x] == -1:
            return []

        #Cells remaining to process
        queuedCells = []
        queuedCells.append([y, x])

        #Cells already visited before
        visitedCells = []
        visitedCells.append([y, x])

        #Cells connectd to the starting seed point
        connectedCells = []
        connectedCells.append([y, x])

        #The 4 directions that define 'adjacent' property
        #Here adjacent cells are vertically or horizontally adjacent
        #For diagonal adjacency there would be 8 directions
        #xDir = [-1, -1, -1, 0, 0, 1, 1, 1]
        #yDir = [-1, 0, 1, -1, 1, -1, 0, 1]
        xDir = [0, 0, -1, 1]
        yDir = [-1, 1, 0, 0]

        #BFS while loop
        #While there are unprocessed cells remaining
        while len(queuedCells) > 0:

            #Get this cell's y and x coordinates
            cell = queuedCells.pop(0)
            y = cell[0]
            x = cell[1]

            #Loop on possible adjacent cells
            for i in range(0, 4):

                #Determine delta y, delta x, new y and new x
                dy = yDir[i]
                dx = xDir[i]
                ny = y + dy
                nx = x + dx

                #Make sure new y and x lie on the grid
                if ny > -1 and ny < self.r and nx > -1 and nx < self.c:

                    #Only process unvisited cells
                    if not visitedCells.count([ny, nx]):

                        #Make a cell visited as soon as you get here
                        visitedCells.append([ny, nx])

                        #Connectedness means that they share the same color, i.e. the same value
                        if self.grid[ny][nx] == self.grid[y][x]:
                            #If connected, add it to unprocessed cells to start traversing from this cell
                            #Also add it to the list of connected region
                            queuedCells.append([ny, nx])
                            connectedCells.append([ny, nx])
                            
        return connectedCells                
                    
    """
    Drops a number of cells from a column when the user clicks on some cell
    This function should be refactored to allow for multiple cells drops at once
    """
    def dropColumn(self, y, x):

        #Shift the column by one cell downwards
        while y > 0:
            self.grid[y][x] = self.grid[y-1][x]
            y = y - 1
        #Assign the upper most cell with -1
        self.grid[0][x] = -1


    """
    column x is not empty
    """
    def dropRow(self, x):
        for i in range(0, self.r):
            for j in range(x, self.c):
                self.grid[i][j] = -1
                if j + 1 < self.c:
                    self.grid[i][j] = self.grid[i][j + 1]

    """
    the user clicks on a cell while playing
    """
    def click(self, y, x):

        #Check for connected region
        connectedCells = self.connectedRegion(y, x)

        #Sort the result
        #This is important so that the dropColumn function can work correctly
        #We should drop cells from above to bottom (from lower index to greater one)
        #Example: if cells (0, 0) and (1, 0) are connected and are to be dropped
        #If we star by dropping cell (1, 0) then cell (0, 0) would be equal to -1
        #If we then attempt to drop cell (0, 0) no effect will happen
        #The other way aroud would work because
        #If we dropped (0, 0) and set it to -1 firstly we would still have cell(1, 0) unchanged
        #Dropping cell (1, 0) then makes sense and does give the expected final results
        connectedCells.sort()
        length = len(connectedCells)

        #Length can be 0, 1 or more
        if length == 0:
            #Click on empty cell
            #I should put a message here
            pass

        else:
            if length == 1:
                #Click on a non-connected cell
                #I should put a message here as well
                pass

            else:
                #Click on a valid cell
                #Drop cells now
                for i in range(0, length):
                    
                    cell = connectedCells[i]
                    y = cell[0]
                    x = cell[1]
                    self.dropColumn(y, x)

                for j in range(self.c - 1, -1, -1):
                    
                    if self.grid[self.r-1][j] == -1:
                        self.dropRow(j);
                    

    """
    A helper function to display a list each row in a separate line
    """
    def display(self):
        for i in range(0, self.r):
            for j in range(0, self.c):
                sys.stdout.write(str(self.grid[i][j]))
                sys.stdout.write('\t')
            print()
        print('***')


#game = SameGame(10, 10, 4)
#game.initGame()
#game.display()

#game.click(3, 2)
#game.display()
