import random
class Board:
    empty_location = "-"
    hit_location = "*"
    miss_location = "X"
    ship_location = "@"
    def __init__(self):
        self.grid = [ [Board.empty_location]*5 for i in range(5)]

    def add_random_ships(self, no_of_ships):
        ships_left = no_of_ships
        while ships_left > 0:

            x = random.randint(0, len(self.grid)-1)
            y = random.randint(0, len(self.grid)-1)
            print(x, y)
            if self.grid[x][y] == Board.empty_location:
                self.grid[x][y] = Board.ship_location
                ships_left -= 1

board = Board()
board.add_random_ships(4)

