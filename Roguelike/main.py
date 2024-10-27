import RoomGen.main as RoomGen
import char

def gameloop(board, player): 
    while True:
        movement = input()
        if (movement == 'w' or
            movement == 'a' or
            movement == 'x' or
            movement == 'd' or
            movement == 'q' or
            movement == 'e' or
            movement == 'y' or
            movement == 'c'):
            board[player.x][player.y] = '░'
            if movement == 'w':
                player.x -= 1
            elif movement == 'a':
                player.y -= 1
            elif movement == 'x':
                player.x += 1
            elif movement == 'd':
                player.y += 1
            elif movement == 'q':
                player.x -= 1
                player.y -= 1
            elif movement == 'e':
                player.x -= 1
                player.y += 1
            elif movement == 'y':
                player.x += 1
                player.y -= 1
            elif movement == 'c':
                player.x += 1
                player.y += 1
        board[player.x][player.y] = player.char
        RoomGen.prntMap(board)

def main():
    """Main function."""
    player = char.pc()
    test = RoomGen.main()
    while test[player.x][player.y] != '░':
        player.reset()
    test[player.x][player.y] = player.char
    RoomGen.prntMap(test)
    
    gameloop(test,player)

    

if __name__ == "__main__":
    main()