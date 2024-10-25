import random as rnd


def create_room(width, height):
    """Create a 2D list representation of a room."""
    room = [[' ' for _ in range(height)] for _ in range(width)]

    for x in range(width):
        for y in range(height):
            room[x][y] = '*'

    return room


def place_rooms(max_x, max_y, room_count, board):
    """Place random rooms on the board."""
    for i in range(room_count):
        room_x = rnd.randint(0, max_x - 21)
        room_y = rnd.randint(0, max_y - 21)

        room_width = rnd.randint(4, 20)
        room_height = rnd.randint(4, 20)

        room = create_room(room_width, room_height)

        for x in range(room_width):
            for y in range(room_height):
                board[room_x + x][room_y + y] = room[x][y]


def empty_borders(board, max_x, max_y):
    """Empty the border tiles around the board."""
    for x in range(max_x):
        for y in range(max_y):
            if x == 0 or y == 0 or x == max_x - 1 or y == max_y - 1:
                board[x][y] = ' '

    return place_walls(board, max_x, max_y)

def fdup_magic(wall_byte):
    #dictionary variables of directions
    south_east = 1
    south = 2
    south_west = 4
    east = 8
    west = 0x10
    north_east = 0x20
    north = 0x40
    north_west = 0x80

    edgeSum = bin(wall_byte & (south | east | west | north)).count('1')
    cornerSum = bin(wall_byte & (south_east | south_west | north_east | north_west)).count('1')
    # 4 3 0 are small
    # edgeSum 4? return 'O'
    # edgeSum 3? return '║' or '═'
    # edgeSum 0? return never any of the above
    # edgeSum >1? then >2? return tested for quality wallpiece
    match edgeSum:
        case 0: # all edges are open space
            # cornerSum == 0 would mean empty space (' ') but that is already the default
            if cornerSum == 1: # exactly one corner is a room tile
                if south_west:
                    return '╗'
                elif south_east:
                    return '╔'
                elif north_west:
                    return '╝'
                elif north_east:
                    return'╚'
            elif cornerSum >= 2: # can find any of the missing border tiles with combinations of exactly 2 corners
                
                # two opposite corners make a cross
                if ((north_west & south_east) |
                (north_east & south_west)):
                    return '╬'
                # north
                elif north_west & north_east:
                    return '╩'
                # south
                elif south_west & south_east:
                    return '╦'
                # west
                elif north_west & south_west:
                    return '╣'
                # east
                elif north_east & south_east:
                    return '╠'
        case 4: # all edges are room tiles
            return 'O'
        case 3: # exactly three edges are room tiles
             
            if (not (west & east)):
                return '═'
            else:
                return '║'
        case 2: # two or less sides open
            if (not (north & south)):
                return '║'
            elif (not (west & east)):
                return '═'
            elif (not (north & west)):
                return '╝'
            elif (not (north & east)):
                return '╚'
            elif (not (south & west)):
                return '╗'
            elif (not (south & east)):
                return '╔'
        case 1: # one edge is a room tile
            if cornerSum == 0: # all corners are open space
                if (not (north & south)):
                    return '║'
                else:
                    return '═'
            elif cornerSum >= 1: # at least one corner is a room tile
                if north:
                    if (south_east | south_west):
                        return '╦'
                    else:
                        return '═'
                if south:
                    if (north_west | north_east):
                        return '╩'
                    else:
                        return '═'
                if west:
                    if (north_east | south_east):
                        return '╠'
                    else:
                        return '║'
                if east:
                    if (north_west | south_west):
                        return '╣'
                    else:
                        return '║'

def place_walls(board, max_x, max_y):
    """Place walls around the rooms."""
    offset_matrix = [
        [-1, -1], [-1, 0], [-1, 1],
        [ 0, -1],          [ 0, 1],
        [ 1, -1], [ 1, 0], [ 1, 1]
    ]

    for x in range(max_x):
        for y in range(max_y):
            wall_byte = 0
            for i, offset in enumerate(offset_matrix):
                nx, ny = x + offset[0], y + offset[1]
                if (nx < 0 or nx >= max_x or ny < 0 or ny >= max_y or board[nx][ny] == '*'):
                    wall_byte |= (1 << (7 + i))
 


            if board[x][y] == ' ':
                if fdup_magic(wall_byte) is not None:
                    board[x][y] = fdup_magic(wall_byte)
    
    return board


def map_init():
    """Initialize the map."""
    max_x = 45
    max_y = 235
    room_count = rnd.randint(1, 10)

    board = [[' ' for _ in range(max_y)] for _ in range(max_x)]

    place_rooms(max_x, max_y, room_count, board)

    return empty_borders(board, max_x, max_y)


def gameloop():
    """Main function."""
    board = map_init()

    for row in board:
        print(''.join(row))


if __name__ == "__main__":
    gameloop()