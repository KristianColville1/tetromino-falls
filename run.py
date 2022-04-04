"""
Tetromino Falls is terminal based game displayed in the browser.
"""

import time
import sys
import curses
import os
import random
from curses import wrapper
from curses.textpad import rectangle

# ternary operator taken from https://www.delftstack.com/howto/python/python-clear-console/
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

# tetromino shapes
SHAPES = {
    'I':[[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]
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
        clearConsole()
        print(f'Oops something went wrong!\n\033[31m{error}\033[0m')
    time.sleep(3)


def get_user_name():
    """
    Gets the users name and checks the database for conflicting names.
    """
    try:
        name = input('Enter your name: ')
        if len(name) < 4 or len(name) > 12:
            raise ValueError(
                'username must be at least 4 characters\n and no more than 12'
            )
    except ValueError as error:
        clearConsole()
        print(f'Invalid username entered: {error}, please try again.\n\n\n')
        return False
    return name


def what_next_user():
    """
    Asks the user what they would like to do next.
    Start the game, load instructions or exit.
    """
    try:
        print(f'\n\nHere are the options available {USER_NAME}:\n')
        print("\t\033[0;33mEnter '\033[31mp\033[0;33m' to play the game.")
        print("\tEnter '\033[31mi\033[0;33m' for instructions..")
        print("\tEnter '\033[31me\033[0;33m' to exit the program.\033[0m")
        user_decision = input(f'\n So what will it be {USER_NAME}?\n ')
        if user_decision not in ('p', 'i', 'e'):
            raise ValueError(
                f"""You need to enter something else as \033[36m{user_decision}\033[0m is invalid"""
            )
    except ValueError as error:
        clearConsole()
        print(f'\n\t\033[31mInvalid data received...\033[0m \n{error}, please try again')
        return False
    return user_decision

def get_next_action():
    """
    Gets the users next action and will decide what route to take.
    Play the game, get instructions or exit program
    """
    # gets and checks the users decision on next actions
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
        file = open('instructions.txt', encoding='utf8')
        instructions = file.read()
        file.close()
        print(f"{instructions}\033[0m")
        if len(instructions) < 1:
            raise IOError(
                "Failed to read instructions from welcome.txt..."
            )
    except IOError as error:
        clearConsole()
        print(f'\033[31m\n{error}\033[0m')



def exit_program():
    """
    Exits the program if the user decides to quit the game.
    """
    clearConsole()
    sys.exit()

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
    Rotate shape takes one argument called shape.
    The argument """

def main(stdscr):
    """
    Main function calls all the necessary functions to run the game.
    """

    #returns the colors for the game objects after initializing the curses
    colors = start_curses()

    stdscr.clear()

    rectangle(stdscr, 1, 4, 21, 42)
    stdscr.refresh()
    # arr = SHAPES['I']

    # for num in arr:
    #     if num == 1:
    #         stdscr.addstr('  ', colors[random.randrange(6)])
    # # stdscr.addstr(f'{arr}', colors[random.randrange(6)])
    # stdscr.refresh()

    x, y = 0, 0
    while True:
        try:
            key = stdscr.getkey()
            if key == 'KEY_RIGHT':
                x += 1
            elif key == 'KEY_LEFT':
                x -= 1
            elif key == 'KEY_DOWN':
                y += 1
            elif key == 'KEY_UP':
                y -= 1
            stdscr.clear()
            stdscr.addstr(y, x, '     ', colors[random.randrange(0, 6)])
            rectangle(stdscr, 1, 4, 21, 42)
            stdscr.refresh()
            if key not in ('KEY_RIGHT', 'KEY_LEFT', 'KEY_DOWN', 'KEY_UP'):
                raise KeyError(
                    f'The {key} not work try something else'
                )
        except KeyError as error:
            stdscr.addstr(20, 20, f'{error}')

    stdscr.getch()


print_welcome_text()

# get and check user name, keep repeating until valid
USER_NAME = get_user_name()
if USER_NAME is False:
    while USER_NAME is False:
        USER_NAME = get_user_name()

get_next_action()
