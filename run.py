import random
class Board:
    empty_location = "-"
    hit_location = "*"
    miss_location = "X"
    ship_location = "@"
    def __init__(self, board_size):
        self.grid = [ [Board.empty_location]*board_size for i in range(board_size)]

    def add_random_ships(self, no_of_ships):
        ships_left = no_of_ships
        while ships_left > 0:

            x = random.randint(0, len(self.grid)-1)
            y = random.randint(0, len(self.grid)-1)
            
            if self.grid[x][y] == Board.empty_location:
                self.grid[x][y] = Board.ship_location
                ships_left -= 1


    
    def display_board(self, hide_ships):
        for row in self.grid:
            for col in row:
                if hide_ships:
                    col = col.replace(board.ship_location, board.empty_location)
                print(col, end=" ")
            print()


board = Board(5)
board.add_random_ships(4)
board.display_board(False)


