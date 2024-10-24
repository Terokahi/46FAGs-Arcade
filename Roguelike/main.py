import random as rnd

def createRoom(x, y):
    """
    Create a 2D list representation of a room.

    Args:
        x (int): The width of the room.
        y (int): The height of the room.

    Returns:
        list: A 2D list representing the room.
    """
    print(f"Creating a room with width {x} and height {y}")
    # Initialize a 2D list to represent the room
    room = [[' ' for _ in range(y)] for _ in range(x)]

    # Fill the room with floor tiles
    for dx in range(x):
        for dy in range(y):
            room[dx][dy] = '*'
    
    print("Room created:")
    for row in room:
        print(''.join(row))
    return room

def placeRooms(maxX, maxY, roomNbr, playAr):
    """
    Place random rooms on the game board.

    Args:
        maxX (int): The maximum x-coordinate of the game board.
        maxY (int): The maximum y-coordinate of the game board.
        roomNbr (int): The number of rooms to place.
        playAr (list): The 2D list representing the game board.

    Returns:
        list: The updated game board with the rooms placed.
    """
    for i in range(roomNbr):
        # Randomly determine the position of the room
        roomX = rnd.randint(0, maxX - 21)
        roomY = rnd.randint(0, maxY - 21)
        print(f"Placing room {i+1} at position ({roomX}, {roomY})")

        # Randomly determine the size of the room
        x = rnd.randint(4, 20)
        y = rnd.randint(4, 20)
        print(f"Room size (width x height): ({x} x {y})")

        # Create the room
        room = createRoom(x, y)
        print(f"Room creation completed at position ({roomX}, {roomY})")

        # Place the room on the game board
        for dx in range(x):
            for dy in range(y):
                playAr[roomX + dx][roomY + dy] = room[dx][dy]
    
    # Place walls around the rooms
    return placeWalls(playAr, maxX, maxY)

def placeWalls(playAr, maxX, maxY):
    """
    Place walls around the rooms.

    Args:
        playAr (list): The 2D list representing the game board.
        maxX (int): The maximum x-coordinate of the game board.
        maxY (int): The maximum y-coordinate of the game board.

    Returns:
        list: The game board with walls placed.
    """
    # wallTesterMatrix =[ [-1,-1],  [-1, 0],   [-1, +1], [0,-1],     [0,+1],     [+1,-1]  ,[+1, 0],    [+1,+1]]
    # patent pending wall_combiner_3000_tm
    # tryForWalls = 0;
    # for i in wallTesterMatrix.length:
    #  if playAr[wallTesterMatrix[i[0]]][wallTesterMatrix[i[1]]] == '*':
    #   tryForWalls &= 1 << 7 - i
    # prüf ob um den Feld Sterne sind, Wo?
    # 0b00000000 = ' '
    # 0b10000000 = '╝'
    tempAr = playAr
    for x in range(maxX):
        for y in range(maxY):
            # Determine if there are walls needed
            south = False
            north = False
            west = False
            east = False

            # Place walls based on their direction
            if south or north:
                if east or west:
                    if south and east:
                        tempAr[x + 1][y + 1] = '╝'
                        tempAr[x + 1][y] = '═'
                        tempAr[x][y + 1] = '║'
                    elif south and west:
                        tempAr[x - 1][y + 1] = '╗'
                        tempAr[x - 1][y] = '═'
                        tempAr[x][y + 1] = '║'
                    elif north and east:
                        tempAr[x + 1][y - 1] = '╚'
                        tempAr[x + 1][y] = '═'
                        tempAr[x][y - 1] = '║'
                    elif north and west:
                        tempAr[x - 1][y - 1] = '╔'
                        tempAr[x - 1][y] = '═'
                        tempAr[x][y - 1] = '║'
                else:
                    if south:
                        tempAr[x][y + 1] = '║'
                    elif north:
                        tempAr[x][y - 1] = '║'
            else:
                if east:
                    tempAr[x + 1][y] = '═'
                elif west:
                    tempAr[x - 1][y] = '═'
    return tempAr

def checkWalls(playAr):
    """
    Placeholder function for checking walls.

    Args:
        playAr (list): The 2D list representing the game board.
    """
    pass

def gameloop():
    """
    The main game loop.

    This function creates a game board, places
    random rooms on it, and prints the final
    game board.
    """
    # Set the maximum size of the game board
    print("Initializing the game board")
    maxX = 45
    maxY = 235

    # Set the number of rooms
    roomNbr = rnd.randint(1, 10)
    print(f"Number of rooms to create: {roomNbr}")

    # Create a 2D list to represent the game board
    playAr = [[' ' for _ in range(maxY)] for _ in range(maxX)]

    print(f"Game board size: {len(playAr)} x {len(playAr[0])}")
    playAr = placeRooms(maxX, maxY, roomNbr, playAr)

    # Place outer walls
    for x in range(maxX):
        for y in range(maxY):
            if x == 0:
                playAr[x][y] = '═'
            if y == 0:
                playAr[x][y] = '║'
            if x == maxX - 1:
                playAr[x][y] = '═'
            if y == maxY - 1:
                playAr[x][y] = '║'
            if x == 0 and y == 0:
                playAr[x][y] = '╔'
            if x == maxX - 1 and y == maxY - 1:
                playAr[x][y] = '╝'
            if x == 0 and y == maxY - 1:
                playAr[x][y] = '╗'
            if y == 0 and x == maxX - 1:
                playAr[x][y] = '╚'

    # Print the game board
    print("Final game board:")
    for row in playAr:
        print(''.join(row))

# Call the game loop
gameloop()

