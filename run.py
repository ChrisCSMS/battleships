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
                    col = col.replace(Board.ship_location, Board.empty_location)
                print(col, end=" ")
            print()

    def add_ship(self, x, y):
        if x < 0 or x >= len(self.grid) or y < 0 or y >= len(self.grid):
            return False
        if self.grid[y][x] == Board.empty_location:
            self.grid[y][x] = Board.ship_location
            return True
        return False
    
    """
    Returns true if input co-ordinates were valid. 
    Returns false if input co-ordinates are invalid.
    """
    def attack_ship(self, x, y):
        if x < 0 or x >= len(self.grid) or y < 0 or y >= len(self.grid):
            return False
        if self.grid[y][x] == Board.empty_location:
            self.grid[y][x] = Board.miss_location
            print("Miss!")
            return True
        elif self.grid[y][x]  == Board.ship_location:
            self.grid[y][x] = Board.hit_location
            print("Hit!")
            return True
        return False

    def has_ships_left(self):
        return str(self.grid).count(Board.ship_location) > 0

def add_player_ships(board, no_of_player_ships):
    board.display_board(False)
    print("Enter your next ship's co-ordinates (ex. 'a1','b4')")
    player_ships_left = no_of_player_ships
    while player_ships_left > 0:
        processed_input = get_inputted_coordinates()
        if processed_input != None and board.add_ship(processed_input["x"], processed_input["y"]):
            player_ships_left -= 1
            print()
            board.display_board(False)
            print()
        else:
            print("Invalid Input")

def get_inputted_coordinates():
    user_input = input("Ship co-ordinate: ")
    processed_input = process_input(user_input)
    return processed_input

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

def battle(player_board, cpu_board):
    while player_board.has_ships_left() and cpu_board.has_ships_left():
        print()
        print("Player Board:")
        player_board.display_board(False)
        print()
        print("CPU Board:")
        cpu_board.display_board(True)
        print()
        print("Enter co-ordinates to attack: (ex. 'a1','b4')")
        coords = get_inputted_coordinates()
        if coords != None and cpu_board.attack_ship(coords["x"], coords["y"]):
            while True:
                x = random.randint(0, len(player_board.grid)-1)
                y = random.randint(0, len(player_board.grid)-1)
                if player_board.attack_ship(x,y):
                    break
    print()
    print("Player Board:")
    player_board.display_board(False)
    print()
    print("CPU Board:")
    cpu_board.display_board(True)



def new_game():
    cpu_board = Board(5)
    cpu_board.add_random_ships(4)
    
    player_board = Board(5)
    
    print("Welcome to Battleships!")
    print("-" * 25)
    print("Would you like to place your ships(y) or randomize them(n)?")
    
    response = input("(y/n) ")
    while response != "y" and response != "n":
        print("Invalid input, type y for yes or n for no")
        response = input("(y/n) ")
    if response == "y":
        clear_screen()
        add_player_ships(player_board, 4)
    else:     
        player_board.add_random_ships(4)

    clear_screen()
    print("Ships have been placed.")
    print("Starting game...")

    battle(player_board, cpu_board)

def clear_screen():
    print("\n"*50) 



new_game()
