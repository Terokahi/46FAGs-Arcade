import random as rnd
"""
Code may or may not have been influenced by:
Divine intervention
Aliens
Cosmic Rays
and Puppys and kittens
"""
def create_room(width, height):
    """Create a 2D list representation of a room."""
    # Initialize a room filled with space characters
    room = [[' ' for _ in range(height)] for _ in range(width)]

    # Fill the entire room with '░' to represent the room space
    for x in range(width):
        for y in range(height):
            room[x][y] = '░'

    return room

def place_rooms(max_x, max_y, room_count, board):
    """Place random rooms on the board."""
    for i in range(room_count):
        # Randomly select a position for the top-left corner of the room
        room_x = rnd.randint(0, max_x - 21)
        room_y = rnd.randint(0, max_y - 21)

        # Randomly determine the room's dimensions
        room_width = rnd.randint(4, 20)
        room_height = rnd.randint(4, 20)

        # Create the room with the specified dimensions
        room = create_room(room_width, room_height)

        # Place the room onto the board at the determined position
        for x in range(room_width):
            for y in range(room_height):
                board[room_x + x][room_y + y] = room[x][y]

def empty_borders(board, max_x, max_y):
    """Empty the border tiles around the board."""
    for x in range(max_x):
        for y in range(max_y):
            # Empty the edges of the board by setting them to space
            if x == 0 or y == 0 or x == max_x - 1 or y == max_y - 1:
                board[x][y] = ' '

    # Add walls around the rooms after emptying borders
    return place_walls(board, max_x, max_y)

def fdup_magic(dir_byte):
    """Determine the wall piece to place based on the direction byte."""
    # Extract bits representing directions from dir_byte
    directions = [(dir_byte >> i) & 1 for i in range(8)]
    south_east, south, south_west, east, west, north_east, north, north_west = directions

    # Masks for identifying edge and corner connections
    edge_mask = 0x5a    # Binary: 01011010
    corner_mask = 0xa5  # Binary: 10100101

    # Count the number of connected edges and corners
    edge_sum = bin(dir_byte & edge_mask).count('1')
    corner_sum = bin(dir_byte & corner_mask).count('1')

    # Determine the appropriate wall piece based on the sums
    if edge_sum == 4:
        return 'O'  # All edges connected
    elif edge_sum == 3:
        # Three edges connected; determine if horizontal or vertical
        return '═' if not (west & east) else '║'
    elif edge_sum == 2:
        # Two edges connected; check specific pairs
        corner_edges = [
            ((west & east), '║'),
            ((north & south) , '═'),
            ((south & east), '╝'),
            ((south & west), '╚'),
            ((north & east), '╗'),
            ((north & west), '╔')
        ]
        return next(symbol for case, symbol in corner_edges if case)
    elif edge_sum == 1:
        # Single edge connection, consider corners
        if corner_sum == 0:
            return '║' if (north | south) else '═'
        elif corner_sum >= 1:
            t_edges = [
                (north & (south_east | south_west), '╦'),
                (south & (north_east | north_west), '╩'),
                (west & (north_east | south_east), '╠'),
                (east & (north_west | south_west), '╣'),
                (north | south, '═'),
                (west | east, '║')
            ]
            return next(symbol for case, symbol in t_edges if case)
    elif edge_sum == 0:
        # No edges connected, check corners
        if corner_sum == 1:
            corners = [south_east, south_west, north_east, north_west]
            return ['╔','╗', '╚', '╝'][corners.index(1)]
        elif corner_sum >= 2:
            # Opposite corners make a cross
            if (north_west & south_east) or (north_east & south_west):
                return '╬'
            t_pairs = [
                (north_west & north_east, '╩'),
                (south_west & south_east, '╦'),
                (north_west & south_west, '╣'),
                (north_east & south_east, '╠')
            ]
            return next(symbol for pair, symbol in t_pairs if pair)

def place_walls(board, max_x, max_y):
    """
    Place walls around the rooms.
    """
    # Define relative positions to check for neighbors
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]

    for x in range(max_x):
        for y in range(max_y):
            dir_byte = 0
            # Check each neighbor and update dir_byte
            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                if (
                    nx < 0 or nx >= max_x or
                    ny < 0 or ny >= max_y or
                    board[nx][ny] == '░'
                ):
                    dir_byte |= (1 << (7 - i))

            # If the current position is empty and has neighboring rooms, place a wall
            if board[x][y] == ' ' and dir_byte:
                board[x][y] = fdup_magic(dir_byte)

    return board

def map_init():
    """Initialize the map."""
    max_x = 45
    max_y = 235
    room_count = rnd.randint(1, 25)

    # Create an empty board
    board = [[' ' for _ in range(max_y)] for _ in range(max_x)]

    # Place rooms on the board
    place_rooms(max_x, max_y, room_count, board)

    # Empty the borders and place walls
    return empty_borders(board, max_x, max_y)

def main():
    """Main function."""
    board = map_init()

    # Print the board row by row
    for row in board:
        print(''.join(row))

if __name__ == "__main__":
    main()

