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
            
            if self.grid[y][x] == Board.empty_location:
                self.grid[y][x] = Board.ship_location
                ships_left -= 1

    def display_board(self, hide_ships):
        print("  A B C D E")
        i = 1
        for row in self.grid:
            print(i, end=" ")
            i += 1
            for col in row:
                if hide_ships:
                    col = col.replace(board.ship_location, board.empty_location)
                print(col, end=" ")
            print()

    def add_ship(self, x, y):
        if x < 0 or x >= len(self.grid) or y < 0 or y >= len(self.grid):
            return False
        if self.grid[y][x] == Board.empty_location:
            self.grid[y][x] = Board.ship_location
            return True
        return False


def add_player_ships(board, no_of_player_ships):
    board.display_board(False)
    print("Enter your ships first co-ordinates (ex. 'a1','b4')")
    player_ships_left = no_of_player_ships
    while player_ships_left > 0:
        user_input = input("Ship co-ordinate: ")
        processed_input = process_input(user_input)
        if processed_input != None and board.add_ship(processed_input["x"], processed_input["y"]):
            player_ships_left -= 1
            board.display_board(False)
        else:
            print("Invalid Input")

def process_input(input):
    if len(input) == 2:
        if input[0].isalpha():
            if input[1].isnumeric():
                x = convert_letter_to_int(input[0])
                y = int(input[1])-1
                return {"x":x,"y":y}
    return None

def convert_letter_to_int(input):
    letter = input.upper()
    A = ord('A')
    letter_value = ord(letter)
    return letter_value - A

cpu_board = Board(5)
player_board = Board(5)
cpu_board.add_random_ships(4)
add_player_ships(player_board, 4)


