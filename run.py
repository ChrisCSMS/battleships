import random
from colorama import Fore


class Board:
    """
    Represents the board and the current state of it's cells
    (empty, hit, missed, ship).
    It contains functions to change the state of the board such as adding ships
    and attempting attacks.
    It can display the board to the terminal.
    """
    empty_loc = "-"
    hit_loc = "*"
    miss_loc = "X"
    ship_loc = "@"

    def __init__(self, board_size):
        self.grid = [[Board.empty_loc]*board_size for i in range(board_size)]

    def add_random_ships(self, no_of_ships):
        ships_left = no_of_ships
        while ships_left > 0:

            x = random.randint(0, len(self.grid)-1)
            y = random.randint(0, len(self.grid)-1)

            if self.grid[y][x] == Board.empty_loc:
                self.grid[y][x] = Board.ship_loc
                ships_left -= 1

    def display_board(self, hide_ships):
        print("  A B C D E")
        i = 1
        for row in self.grid:
            print(i, end=" ")
            i += 1
            for col in row:
                if hide_ships:
                    col = col.replace(Board.ship_loc, Board.empty_loc)
                if col == Board.ship_loc:
                    col = color(Fore.CYAN, col)
                elif col == Board.hit_loc:
                    col = color(Fore.RED, col)
                elif col == Board.miss_loc:
                    col = color(Fore.MAGENTA, col)
                print(col, end=" ")
            print()

    def add_ship(self, x, y):
        if x < 0 or x >= len(self.grid) or y < 0 or y >= len(self.grid):
            return False
        if self.grid[y][x] == Board.empty_loc:
            self.grid[y][x] = Board.ship_loc
            return True
        return False

    def attack_ship(self, x, y):
        """
        Handles attacking the board at the given coordinates.
        Returns true if input co-ordinates were valid.
        Returns false if input co-ordinates are invalid.
        """
        if x < 0 or x >= len(self.grid) or y < 0 or y >= len(self.grid):
            return False
        if self.grid[y][x] == Board.empty_loc:
            self.grid[y][x] = Board.miss_loc
            return True
        elif self.grid[y][x] == Board.ship_loc:
            self.grid[y][x] = Board.hit_loc
            return True
        return False

    def has_ships_left(self):
        return str(self.grid).count(Board.ship_loc) > 0


def color(color, str):
    return color + str + Fore.WHITE


def add_player_ships(board, no_of_player_ships):
    """
    Gets input from the player for where they should add their ships.
    The ship is added to the input coordinates if they are valid.
    """
    board.display_board(False)
    print("Enter your next ship's co-ordinates (ex. 'a1','b4')")
    player_ships_left = no_of_player_ships
    while player_ships_left > 0:
        input = get_inputted_coordinates()
        if input is not None and board.add_ship(input["x"], input["y"]):
            player_ships_left -= 1
            print()
            board.display_board(False)
            print()
        else:
            print(color(Fore.RED, "Enter a position on the grid."))


def get_inputted_coordinates():
    user_input = input("Ship co-ordinate: ")
    processed_input = process_input(user_input)
    return processed_input


def process_input(input):
    """
    Verifies that the input is in a Letter-Number format such as A2
    Returns a dictionary of the input as x and y coordinates
    """
    if len(input) == 2:
        if input[0].isalpha():
            if input[1].isnumeric():
                x = convert_letter_to_int(input[0])
                y = int(input[1])-1
                return {"x": x, "y": y}
    print(color(Fore.RED, "Please enter a letter and number (ex. 'a2')"))
    return None


def convert_letter_to_int(input):
    """
    Converts a character to an integer index by offsetting it
    with the value of the 'A' character
    """
    letter = input.upper()
    A = ord('A')
    letter_value = ord(letter)
    return letter_value - A


def battle(player_board, cpu_board):
    """
    Handles the battle mechanics for the game.
    It displays the current state of the boards;
    and allows the player and CPU to take their turns.
    """
    turn = 1
    while player_board.has_ships_left() and cpu_board.has_ships_left():
        print(f"Turn {turn}")
        print()
        print("Player Board:")
        player_board.display_board(False)
        print()
        print("CPU Board:")
        cpu_board.display_board(True)
        print()
        print("Enter co-ordinates to attack: (ex. 'a1','b4')")
        coords = get_inputted_coordinates()
        if coords is not None:
            if cpu_board.attack_ship(coords["x"], coords["y"]):
                clear_screen()
                cell = cpu_board.grid[coords["y"]][coords["x"]]
                result = "hit!" if cell == Board.hit_loc else "missed!"
                print(f"Player {result}")
                while True:
                    if not cpu_board.has_ships_left():
                        break
                    x = random.randint(0, len(player_board.grid)-1)
                    y = random.randint(0, len(player_board.grid)-1)
                    if player_board.attack_ship(x, y):
                        cell = player_board.grid[y][x]
                        result = None
                        if cell == Board.hit_loc:
                            result = "hit!"
                        else:
                            result = "missed!"
                        print(f"CPU {result}")
                        turn += 1
                        break

    print()
    print("Player Board:")
    player_board.display_board(False)
    print()
    print("CPU Board:")
    cpu_board.display_board(True)


def play_game():
    """
    Initializes and runs the game and handles restarting
    the game when it has finished.
    """
    cpu_board = Board(5)
    cpu_board.add_random_ships(4)

    player_board = Board(5)
    print(color(Fore.CYAN, r"""
     ___           _    _    _
    (  _`\        ( )_ ( )_ (_ )              ( )
    | (_) )   _ _ | ,_)| ,_) | |    __    ___ | |__  (_) _ _     ___
    |  _ <' /'_` )| |  | |   | |  /'__`\/',__)|  _ `\| |( '_`\ /',__)
    | (_) )( (_| || |_ | |_  | | (  ___/\__, \| | | || || (_) )\__, \
    (____/'`\__,_)`\__)`\__)(___)`\____)(____/(_) (_)(_)| ,__/'(____/
                                                        | |
                                                        (_)
    """))
    print(color(Fore.BLUE, "Welcome to Battleships!"))
    print("-" * 25)
    print("Would you like to view the tutorial? (y/n) ")
    tutorial = get_input_answer()
    if tutorial == "y":

        print(color(Fore.CYAN, r"""
         ___________________________________________________________________
        |                                                                   |
        |                           Battleships                             |
        |___________________________________________________________________|
        |                                                                   |
        | Battleships is a game where you attack enemy ships                |
        | by inputting co-ordinates.                                        |
        | The player can't see where the enemy ships are placed.            |
        | Co-ordinates range from 1-5 and A-E and are inputted as 'a2'      |
        | Whoever destroys the others ships first is the winner.            |
        |                                                                   |
        |___________________________________________________________________|

        """))
    print("Would you like to place your ships(y) or randomize them(n)?")

    response = get_input_answer()
    if response == "y":
        clear_screen()
        add_player_ships(player_board, 4)
    else:
        player_board.add_random_ships(4)

    clear_screen()
    print("Ships have been placed.")
    print("Starting game...")

    battle(player_board, cpu_board)

    print("Game Over!")

    if player_board.has_ships_left():
        print("You win!")
    else:
        print("CPU wins!")
    print()
    print("Would you like to play again? (y/n)")
    answer = get_input_answer()
    if answer == "y":
        clear_screen()
        print("Starting new game...")
        play_game()
    else:
        print("Thanks for playing!")


def get_input_answer():
    """
    Gets a valid Yes(y) or No(n) input from the user
    """
    response = input("(y/n) ")
    while response != "y" and response != "n":
        print(color(Fore.RED, "Invalid input, type y for yes or n for no"))
        response = input("(y/n) ")
    return response


def clear_screen():
    """
    Clears the screen by adding empty space to make the terminal more readable.
    """
    print("\n"*50)


play_game()
