#######################
#asmaa.magdi@gmail.com#
#######################


import random

MAX_COLORS = 6

"""
Initializes a random same game grid
r: number of rows
c: number of columns
x: number of different colors
"""
def initGameGrid(r, c, x):
    if x > MAX_COLORS:
        x = MAX_COLORS
    game = []
    for i in range(0, r):
        row = []
        for j in range(0, c):
            row.append(random.randint(0, x - 1))
        game.append(row)
    return game


"""
Finds a connected region from a seed point
Used to determine how many (and which) cells to remove, if any, when the user clicks on a cell (y, x)
Based of a BFS algorithm
"""
def connectedRegion(y, x, gameGrid):

    r = len(gameGrid)

    if r == 0:
        return []
    c = len(gameGrid[0])
    
    if gameGrid[y][x] == -1:
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
            if ny > -1 and ny < r and nx > -1 and nx < c:

                #Only process unvisited cells
                if not visitedCells.count([ny, nx]):

                    #Make a cell visited as soon as you get here
                    visitedCells.append([ny, nx])

                    #Connectedness means that they share the same color, i.e. the same value
                    if gameGrid[ny][nx] == gameGrid[y][x]:
                        #If connected, add it to unprocessed cells to start traversing from this cell
                        #Also add it to the list of connected region
                        queuedCells.append([ny, nx])
                        connectedCells.append([ny, nx])
                        
    return connectedCells                
                
"""
Drops a number of cells from a column when the user clicks on some cell
This function should be refactored to allow for multiple cells drops at once
"""
def dropColumn(y, x, gameGrid):

    #Shift the column by one cell downwards
    while y > 0:
        gameGrid[y][x] = gameGrid[y-1][x]
        y = y - 1
    #Assign the upper most cell with -1
    gameGrid[0][x] = -1

    return gameGrid

"""
the user clicks on a cell while playing
"""
def click(y, x, gameGrid):

    #Check for connected region
    connectedCells = connectedRegion(y, x, gameGrid)

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

                gameGrid = dropColumn(y, x, gameGrid)
                
    return gameGrid

"""
A helper function to display a list each row in a separate line
"""
def display(gameGrid):
    r = len(gameGrid)
    for i in range(0, r):
        print(gameGrid[i])
    print('***')


#Sampel usage
gameGrid = initGameGrid(5, 5, 3)
display(gameGrid)

gameGrid = click(3, 2, gameGrid)
display(gameGrid)

gameGrid = click(0, 1, gameGrid)
display(gameGrid)

gameGrid = click(1, 4, gameGrid)
display(gameGrid)
