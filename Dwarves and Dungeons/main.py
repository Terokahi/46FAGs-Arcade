import roomGen
import char

def gameloop(board, player): 
    while True:
        x, y = char.move()
        if board[player.x + x][player.y + y] != '░':
            x,y = 0, 0
        board[player.x][player.y] = '░'
        player.x += x
        player.y += y
        board[player.x][player.y] = player.char

def main():
    """Main function."""
    player = char.pc()
    map = roomGen.main()
    
    while map[player.x][player.y] != '░':
        player.reset()
    map[player.x][player.y] = player.char
    roomGen.prntMap(map)
    
    gameloop(map,player)

    

if __name__ == "__main__":
    main()