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
    return emptyBorders(playAr, maxX, maxY)

def emptyBorders(playAr, maxX, maxY):
    """
    Place border tiles around the game board.

    Args:
        maxX (int): The maximum x-coordinate of the game board.
        maxY (int): The maximum y-coordinate of the game board.
        playAr (list): The 2D list representing the game board.

    Returns:
        list: The updated game board with the border tiles placed.
    """
    for x in range(maxX):
        for y in range(maxY):
            if x == 0 or y == 0 or x == maxX - 1 or y == maxY - 1:
                playAr[x][y] = ' '

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
    # prüf ob um den Feld Sterne sind, Wo?
    # 0b00000000 = ' '
    # 0b10000000 = '╝''╔'
    # 0b01000000 = '═'
    # 0b00100000 = '║'
    # 0b00010000 = '╚'
    # 0b00001000 = '╔'
    # 0b00000100 = '╠''╝'
    # 0b00000010 = '╦''╚'
    # 0b00000001 = '╩'
    # 0b11000000 = '╗'

    # patent pending wall_combiner_3000_tm
    wallTesterMatrix =[[-1,-1], [-1, 0], [-1, +1], [0,-1], [0,+1], [+1,-1], [+1, 0], [+1,+1]]
    


    for x in range(maxX):
        for y in range(maxY):
            tryForWalls = 0

            top_left = False
            top = False
            top_right = False
            left = False
            right = False
            bottom_left = False
            bottom = False
            bottom_right = False

            for i in range(len(wallTesterMatrix)):
                # Test Oob
                if ((x + wallTesterMatrix[i][0] < 0 or x + wallTesterMatrix[i][0] >= maxX or y + wallTesterMatrix[i][1] < 0 or y + wallTesterMatrix[i][1] >= maxY) 
                    # Test if already used
                    or playAr[x + wallTesterMatrix[i][0]][y + wallTesterMatrix[i][1]] == '*'):
                
                    match i:
                        case 0:
                            top_left = True
                        case 1:
                            top = True
                            top_left = True
                            top_right = True
                        case 2:
                            top_right = True
                        case 3:
                            left = True
                            top_left = True
                            bottom_left = True
                        case 4:
                            right = True
                            top_right = True
                            bottom_right = True
                        case 5:
                            bottom_left = True
                        case 6:
                            bottom = True
                            bottom_left = True
                            bottom_right = True
                        case 7:
                            bottom_right = True
            edgeSum = top + bottom + left + right
            cornerSum = top_left + top_right + bottom_left + bottom_right

            if playAr[x][y] == ' ':
                # all four sides used
                if (top and bottom and left and right):
                    if (top_left and top_right and bottom_left and bottom_right):
                        playAr[x][y] = "╬"
                    else:
                        playAr[x][y] = 'O'
                # one side open
                if (edgeSum == 3):
                    if (not top):
                        playAr[x][y] = '║'
                    if (not bottom):
                        playAr[x][y] = '║'
                    if (not left):
                        playAr[x][y] = '═'
                    if (not right):
                        playAr[x][y] = '═'
                # two sides open
                if (edgeSum == 2):
                    if (not top and not bottom):
                        playAr[x][y] = '║'
                    if (not left and not right):
                        playAr[x][y] = '═'
                    if ( not top and not left):
                        playAr[x][y] = '╝'
                    if ( not top and not right):
                        playAr[x][y] = '╚'
                    if ( not bottom and not left):
                        playAr[x][y] = '╗'
                    if ( not bottom and not right):
                        playAr[x][y] = '╔'
                # three sides open
                if (edgeSum == 1):
                    if cornerSum >= 2 and edgeSum:
                        if (top_left and bottom_right or
                            top_right and bottom_left):
                            playAr[x][y] = '╬'
                        if top_left and top_right:
                            playAr[x][y] = '╩'
                        if bottom_left and bottom_right:
                            playAr[x][y] = '╣'
                        if top_left and bottom_left:
                            playAr[x][y] = '╠'
                        if top_right and bottom_right:
                            playAr[x][y] = '╦'
                    elif ((not top and not bottom and not left) ^ (not top and not bottom and not right)):
                        playAr[x][y] = '║'
                    elif ((not top and not left and not right) ^ (not bottom and not left and not right)):
                        playAr[x][y] = '═'


                if edgeSum == 0:
                    if cornerSum == 1:
                        if bottom_left:
                            playAr[x][y] = '╗'
                        if bottom_right:
                            playAr[x][y] = '╔'
                        if top_left:
                            playAr[x][y] = '╝'
                        if top_right:
                            playAr[x][y] =  '╚'
                    if cornerSum >= 2:
                        if (top_left and bottom_right or
                            top_right and bottom_left):
                            playAr[x][y] = '╬'
                        if top_left and top_right:
                            playAr[x][y] = '╩'
                        if bottom_left and bottom_right:
                            playAr[x][y] = '╣'
                        if top_left and bottom_left:
                            playAr[x][y] = '╠'
                        if top_right and bottom_right:
                            playAr[x][y] = '╦'
    return playAr

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
    maxX = 45 # height def 45
    maxY = 235 # width def 235

    # Set the number of rooms
    roomNbr = rnd.randint(1, 10)
    print(f"Number of rooms to create: {roomNbr}")

    # Create a 2D list to represent the game board
    playAr = [[' ' for _ in range(maxY)] for _ in range(maxX)]

    print(f"Game board size: {len(playAr)} x {len(playAr[0])}")
    playAr = placeRooms(maxX, maxY, roomNbr, playAr)

    # Print the game board
    print("Final game board:")
    for row in playAr:
        print(''.join(row))

# Call the game loop
gameloop()

