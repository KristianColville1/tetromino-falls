"""
Tetromino Falls is terminal based game displayed in the browser.
"""

import time
import sys
import curses
import random
from curses import wrapper
from curses.textpad import rectangle
import console
from user_name import User




# tetromino shapes
SHAPES = {
    'I':[[2, 3], [2, 3], [2, 3], [2, 3]]
        ,
    'J':[[0, 1, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0]]
        ,
    'L':[[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
        ,
    'O':[[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
        ,
    'T':[[1, 1, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        ,
    'S':[[0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        ,
    'Z':[[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
}

def print_welcome_text():
    """
    Prints welcome text to terminal for user and waits for 3 seconds before moving on.
    """
    try:
        file = open('welcome-msg.txt', encoding='utf8')
        message = file.read()
        print('\n\n\n\033[31m' + message + '\033[0m\n\n\n')
        file.close()
        if len(message) < 1:
            raise IOError(
                'An error occurred fetching the welcome message.. sorry about that..'
            )
    except IOError as error:
        console.clear_console()
        print(f'Oops something went wrong!\n\033[31m{error}\033[0m')
    time.sleep(3)


def get_user_name():
    """
    Gets the users name and checks the database for conflicting names.
    """



def what_next_user():
    """
    Asks the user what they would like to do next.
    Start the game, load instructions or exit.
    """
    try:
        print(f'\n\nHere are the options available {USER_NAME.user_name}:\n')
        print("\t\033[0;33mEnter '\033[31mp\033[0;33m' to play the game.")
        print("\tEnter '\033[31mi\033[0;33m' for instructions..")
        print("\tEnter '\033[31me\033[0;33m' to exit the program.\033[0m")
        user_decision = input(f'\n So what will it be {USER_NAME.user_name}?\n ')
        if user_decision not in ('p', 'i', 'e'):
            raise ValueError(
                f"""You need to enter something else as \033[36m{user_decision}\033[0m is invalid"""
            )
    except ValueError as error:
        console.clear_console()
        print(f'\n\t\033[31mInvalid input received...\033[0m \n{error}, please try again')
        return False
    return user_decision

def get_next_action():
    """
    Gets the users next action and will decide what route to take.
    Play the game, get instructions or exit program
    """
    # gets and checks the users decision on next actions
    console.clear_console()
    decision = what_next_user()
    if decision is False:
        while decision is False:
            decision = what_next_user()

    if decision == 'p':
        start_game()
    elif decision == 'i':
        get_instructions()
    else:
        exit_program()

def start_game():
    """
    Starts the game calls the main function.
    """
    wrapper(main)


def get_instructions():
    """
    When called it will get instructions on how to play the game.
    """
    print('\033[0;33m')
    try:
        console.clear_console()
        file = open('instructions.txt', encoding='utf8')
        instructions = file.read()
        file.close()
        print(f"{instructions}\033[0m")
        try:
            read_instructions = input('\033[31m\nEnter "y" and hit enter to continue: \033[0m')
            if read_instructions not in ('Y', 'y'):
                raise ValueError(
                    '\033[36m\nEnter the letter y for yes or n for no\n\033[0m'
                )
        except ValueError as error:
            print(error)
            time.sleep(2)
            console.clear_console()
            get_instructions()
        if len(instructions) < 1:
            raise IOError(
                "Failed to read instructions from welcome.txt..."
            )
    except IOError as error:
        console.clear_console()
        print(f'\033[31m\n{error}\033[0m')
    get_next_action()


def exit_program():
    """
    Exits the program if the user decides to quit the game.
    Loops using recursion until valid input is entered.
    """
    try:
        check_input = 'Are you absolutely sure you want to exit the program? y/n '
        user_decision = input(f'\033[0;31m{check_input}:\033[0m')
        if user_decision not in ('y', 'n'):
            raise ValueError(
                f'\n\033[31m{user_decision}\033[0m is not valid input, try again...\n'
            )
        if user_decision == 'n':
            get_next_action()
        elif user_decision == 'y':
            console.clear_console()
            thanks_for_playing()
            sys.exit()
    except ValueError as error:
        print(f'{error}')
        exit_program()


def thanks_for_playing():
    """
    When the user decides to quit the game this message is displayed in the terminal.
    """
    try:
        file = open('goodbye.txt', encoding='utf8')
        message = file.read()
        console.clear_console()
        print(message)
        time.sleep(4)
        file.close()
        if file is None:
            raise IOError(
                'The thank you message failed to display...'
            )
    except IOError as error:
        print(f"An error has occurred..\n {error}")


def start_curses():
    """
    Initializes the curses objects.
    Specifically allows the colors to be used and windows to be created.
    Returns the colors after curses color pairs are initialized.
    """
    curses.initscr()

    # Allows the curses colors to be accessed and used
    curses.start_color()

    # background curses color pairs initialized
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_CYAN)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_YELLOW)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_WHITE)

    # text curses color pairs initialized
    curses.init_pair(8, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(9, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(10, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(11, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(12, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(13, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(14, curses.COLOR_WHITE, curses.COLOR_BLACK)

    # background colors with white text
    blue = curses.color_pair(1)
    cyan = curses.color_pair(2)
    red = curses.color_pair(3)
    yellow = curses.color_pair(4)
    green = curses.color_pair(5)
    purple = curses.color_pair(6)
    white = curses.color_pair(7)

    colors = [blue, cyan, red, yellow, green, purple, white]

    return colors


def rotate_shape(shape_array):
    """
    Rotate shape takes one argument called shape_array.
    The argument returns the shape array after rotating it counter clockwise.
    """
    rows, cols = len(shape_array), len(shape_array[0])
    rotated_shape = [[None] * rows for _ in range(cols)]


    for col in range(cols):
        for row in range(rows - 1, -1, -1):
            rotated_shape[cols - col - 1][row] = shape_array[rows][cols]

    return rotated_shape


def get_random_shape():
    """
    When called it returns a random shape from SHAPES.
    The returned data is a 2D array.
    """
    keys = ['I', 'J', 'L', 'O', 'T', 'S', 'Z']

    rand_shape = SHAPES[keys[random.randrange(7)]]
    return rand_shape


def create_game_grid():
    """
    Creates a matrix for the game grid for Tetromino Falls"""
    grid_matrix = []
    for j in range(21):
        grid_matrix.append([])
        for _ in range(21):
            grid_matrix[j].append([0])
    return grid_matrix


def main(stdscr):
    """
    Main function calls all the necessary functions to run the game.
    """
    #returns the colors for the game objects after initializing the curses
    colors = start_curses()

    stdscr.clear()
    rectangle(stdscr, 1, 4, 21, 42)
    stdscr.refresh()
    shape = SHAPES['I']
    color = colors[random.randrange(6)]
    y_axis, x_axis = 0, 0

    # creates a matrix for the game grid to manipulate
    game_grid = create_game_grid()
    while True:
        try:
            y_axis += 1
            time.sleep(0.3)
            key = stdscr.getkey()
            if key == 'KEY_RIGHT':
                x_axis += 1
            elif key == 'KEY_LEFT':
                x_axis -= 1
            elif key == 'KEY_DOWN':
                y_axis += 1
            elif key == 'KEY_UP':
                y_axis -= 1
            stdscr.clear()
            rectangle(stdscr, 1, 4, 21, 42)
            stdscr.refresh()
            if key not in ('KEY_RIGHT', 'KEY_LEFT', 'KEY_DOWN', 'KEY_UP'):
                raise KeyError(
                    f'The {key} not work try something else'
                )
        except KeyError as error:
            stdscr.addstr(20, 30, f'{error}')

    stdscr.getch()


print_welcome_text()

# get and check user name, keep repeating until valid
USER_NAME = User()
print(USER_NAME.user_name)

get_next_action()
